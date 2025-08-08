"""
rsearch_module

This module provides functionality for semantic search using Redis and OpenAI's LLM.
It includes methods for embedding text, querying the LLM, and caching results in Redis.
"""
import os
import time
import numpy as np
from redisvl.extensions.llmcache import SemanticCache
from openai import OpenAI
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Connect to Redis Cloud (replace with your credentials)
load_dotenv()  # Loads variables from a .env file into environment

RDS_URI = os.environ.get("RDS_URI")  # Make sure to add RDS_URI=<your_redis_url> to your .env file
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")  # Make sure to add your OpenAI API key

if not RDS_URI:
    raise ValueError("RDS_URI environment variable not set")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Initialize OpenAI client
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Use a model that produces 768-dimensional embeddings to match Redis cache configuration
embedder = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

# Initialize cache with proper error handling for dimension mismatches
try:
    cache = SemanticCache(
        name="llmcache",
        redis_url=RDS_URI,
        distance_threshold=0.1  # Adjust for strictness of semantic similarity
    )
except Exception as e:
    print(f"Warning: Error initializing cache: {e}")
    # If cache initialization fails, we'll create a fallback later
    cache = None
def check_openai_status():
    """
    Check if OpenAI API is accessible and return status information.
    """
    try:
        # Try a minimal API call to check status
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )

        if not response or not response.choices:
            return {"status": "error", "message": "No response from OpenAI API"}
        
        return {"status": "ok", "message": "OpenAI API is accessible"}
    except Exception as e:
        error_str = str(e)
        if "insufficient_quota" in error_str or "429" in error_str:
            return {
                "status": "quota_exceeded", 
                "message": "Quota exceeded. Please check your OpenAI billing.",
                "action_url": "https://platform.openai.com/settings/organization/billing"
            }
        elif "rate_limit" in error_str:
            return {"status": "rate_limited", "message": "Rate limit exceeded. Please wait."}
        elif "authentication" in error_str or "401" in error_str:
            return {"status": "auth_error", "message": "Invalid API key. Check your OPENAI_API_KEY."}
        else:
            return {"status": "error", "message": f"API Error: {e}"}

def embed(text):
    """
    Generate an embedding for the given text using SentenceTransformer.
    Returns a numpy array that can be safely converted to a list.
    """
    if not text:
        raise ValueError("Text for embedding cannot be empty")
    
    try:
        # Get embedding and ensure it's a proper numpy array
        embedding = embedder.encode([text])[0]
        # Ensure it's a proper numpy array (not a weird subclass)
        return np.array(embedding, dtype=np.float32)
    except Exception as e:
        print(f"Error generating embedding: {e}")
        raise

def llm_query_with_retry(prompt, max_retries=3, retry_delay=2):
    """
    Query the LLM with retry logic for rate limits.
    """
    for attempt in range(max_retries):
        try:
            response = openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            error_str = str(e)

            # Don't retry on quota exceeded or auth errors
            if "insufficient_quota" in error_str or "authentication" in error_str:
                raise e

            # Retry on rate limits
            if "rate_limit" in error_str and attempt < max_retries - 1:
                print(f"⏳ Rate limited. Retrying in {retry_delay} seconds... (Attempt {attempt + 1}/{max_retries})")
                time.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
                continue
            # Re-raise the exception if max retries reached
            raise e
        
def llm_query(prompt):
    """
    Query the LLM with the given prompt using the new OpenAI client.
    Includes enhanced error handling for quota issues.
    """
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",  # Using a more cost-effective model
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )

        if not response or not response.choices:
            return {"status": "error", "message": "No response from OpenAI API"}
        return response.choices[0].message.content
    except Exception as e:
        error_str = str(e)

        # Handle specific quota exceeded error
        if "insufficient_quota" in error_str or "429" in error_str:
            print("⚠️  OpenAI API Quota Exceeded!")
            print("🔧 To fix this issue:")
            print("   1. Check your OpenAI billing at: https://platform.openai.com/settings/organization/billing")
            print("   2. Add credits or upgrade your plan")
            print("   3. Ensure your payment method is valid")
            print("   4. Check usage limits in your dashboard")
            return f"[QUOTA_EXCEEDED] Unable to generate response for: '{prompt[:50]}...' - Please check your OpenAI billing."
        
        # Handle rate limit errors
        elif "rate_limit" in error_str:
            print("⚠️  OpenAI API Rate Limit Exceeded!")
            print("💡 Try again in a few seconds...")
            return f"[RATE_LIMITED] Please try again later for: '{prompt[:50]}...'"
        
        # Handle authentication errors
        elif "authentication" in error_str or "401" in error_str:
            print("⚠️  OpenAI API Authentication Error!")
            print("🔧 Check your OPENAI_API_KEY in the .env file")
            return f"[AUTH_ERROR] Invalid API key for: '{prompt[:50]}...'"
        
        # Generic error handling
        else:
            print(f"❌ OpenAI API error: {e}")
            return f"[API_ERROR] Mock response for: '{prompt[:50]}...' (OpenAI API not available)"

def get_cached_or_generate(prompt):
    """
    Checks the semantic cache for the given prompt; 
    if not found, generates a response using LLM with enhanced error handling
    """
    # Only try cache if it's properly initialized
    if cache is not None:
        try:
            embedding = embed(prompt)
            cached = cache.check(prompt, embedding.tolist())
            if cached:
                print("Cache hit!")
                # Handle different return types from cache
                if isinstance(cached, list) and len(cached) > 0:
                    return cached[0].get('response', cached[0]) if isinstance(cached[0], dict) else str(cached[0])
                elif hasattr(cached, 'response'):
                    return cached.response
                else:
                    return str(cached)
        except Exception as e:
            print(f"Cache check error: {e}")

    # Cache miss or cache unavailable - fetch from LLM
    print("Cache miss or unavailable, calling LLM...")
    try:
        embedding = embed(prompt)
        # Try with retry logic first, fall back to basic query if needed
        try:
            result = llm_query_with_retry(prompt)
        except Exception as retry_error:
            print(f"Retry logic failed: {retry_error}")
            result = llm_query(prompt)

        # Store in cache only if cache is available - convert numpy array to list to avoid boolean evaluation issues
        if cache is not None:
            try:
                # Convert numpy array to list to avoid "ambiguous truth value" error
                embedding_list = embedding.tolist() if hasattr(embedding, 'tolist') else embedding
                cache.store(prompt, result, embedding_list)
                print("Result stored in cache successfully!")
            except Exception as store_error:
                error_msg = str(store_error)
                if "Invalid vector dimensions" in error_msg or "Vector dims must be equal" in error_msg:
                    print(f"⚠️  Vector dimension mismatch: {store_error}")
                    print("💡 Consider clearing the Redis cache or using a different embedder model")
                    print(f"   Current embedder produces {len(embedding_list) if hasattr(embedding, 'tolist') else 'unknown'} dimensions")
                else:
                    print(f"Error storing in cache: {store_error}")
                # Continue execution even if caching fails
        else:
            print("Cache not available - result not cached")
            
        return result
    except Exception as e:
        print(f"Error in cache miss handling: {e}")
        # Return the result even if caching fails
        try:
            return llm_query_with_retry(prompt)
        except Exception:
            return llm_query(prompt)
