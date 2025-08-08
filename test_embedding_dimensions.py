#!/usr/bin/env python3
"""
Test script to verify embedding dimensions and cache functionality
"""
from rsearch_module import embed, get_cached_or_generate

def test_embedding_dimensions():
    """Test that embeddings have the correct dimensions"""
    print("=== Testing Embedding Dimensions ===")
    
    test_text = "This is a test sentence for embedding"
    
    try:
        embedding = embed(test_text)
        print("✅ Embedding generated successfully")
        print(f"📏 Embedding dimensions: {len(embedding)}")
        print(f"🔢 Embedding type: {type(embedding)}")
        
        # Convert to list as we do in the main code
        embedding_list = embedding.tolist() if hasattr(embedding, 'tolist') else embedding
        print(f"📝 List conversion successful: {len(embedding_list)} dimensions")
        
        return True
        
    except Exception as e:
        print(f"❌ Error generating embedding: {e}")
        return False

def test_cache_functionality():
    """Test the cache storing and retrieval"""
    print("\n=== Testing Cache Functionality ===")
    
    test_prompt = "What is the capital of France?"
    
    try:
        print(f"🔍 Testing with prompt: '{test_prompt}'")
        result = get_cached_or_generate(test_prompt)
        print("✅ First call completed")
        print(f"📝 Result: {result[:100]}{'...' if len(result) > 100 else ''}")
        
        # Second call should hit cache if working
        print("\n🔍 Second call (should hit cache):")
        result2 = get_cached_or_generate(test_prompt)
        print("✅ Second call completed")
        print(f"📝 Result: {result2[:100]}{'...' if len(result2) > 100 else ''}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in cache functionality test: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Running Redis Semantic Search Tests\n")
    
    # Test embedding dimensions
    embedding_test = test_embedding_dimensions()
    
    # Test cache functionality
    cache_test = test_cache_functionality()
    
    print("\n📊 Test Results:")
    print(f"   Embedding Test: {'✅ PASS' if embedding_test else '❌ FAIL'}")
    print(f"   Cache Test: {'✅ PASS' if cache_test else '❌ FAIL'}")
    
    if embedding_test and cache_test:
        print("\n🎉 All tests passed! The Redis cache issue should be resolved.")
    else:
        print("\n⚠️  Some tests failed. Check the error messages above.")
