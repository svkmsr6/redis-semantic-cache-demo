"""Demo script for Redis Semantic Caching and Similarity Queries"""
import time

# Import the semantic search module
from rsearch_module import get_cached_or_generate

def demo_semantic_caching():
    """
    Demonstrate semantic caching performance by querying the same prompt twice
    and measuring the time difference.
    """

    # Test query
    test_prompt = "What is semantic caching in Redis Cloud?"

    print("=== Redis Semantic Caching Demo ===\n")
    print(f"Test Query: '{test_prompt}'\n")

    # First query - should be a cache miss
    print("🔍 First Query (Cache Miss Expected):")
    start_time = time.time()

    try:
        result1 = get_cached_or_generate(test_prompt)
        first_query_time = time.time() - start_time
        print(f"⏱️  Time taken: {first_query_time:.2f} seconds")
        print(f"📝 Response: {result1[:100]}{'...' if len(result1) > 100 else ''}\n")
    except Exception as e:
        print(f"❌ Error on first query: {e}\n")
        return

    # Small delay to make the demonstration clearer
    time.sleep(1)

    # Second query - should be a cache hit
    print("🔍 Second Query (Cache Hit Expected):")
    start_time = time.time()

    try:
        result2 = get_cached_or_generate(test_prompt)
        second_query_time = time.time() - start_time
        print(f"⏱️  Time taken: {second_query_time:.2f} seconds")
        print(f"📝 Response: {result2[:100]}{'...' if len(result2) > 100 else ''}\n")
    except Exception as e:
        print(f"❌ Error on second query: {e}\n")
        return

    # Performance comparison
    print("📊 Performance Analysis:")
    print(f"   First Query:  {first_query_time:.2f} seconds")
    print(f"   Second Query: {second_query_time:.2f} seconds")

    if second_query_time < first_query_time:
        speedup = first_query_time / second_query_time
        time_saved = first_query_time - second_query_time
        print(f"   🚀 Speedup: {speedup:.1f}x faster")
        print(f"   💰 Time Saved: {time_saved:.2f} seconds")
    else:
        print("   ℹ️  No significant speedup detected (cache might not have been used)")

    print("\n" + "="*50)

def demo_similar_queries():
    """
    Demonstrate semantic similarity by using slightly different but semantically similar queries.
    """

    print("\n=== Semantic Similarity Demo ===\n")

    queries = [
        "How does Redis semantic cache work?",
        "What is the mechanism behind Redis semantic caching?",
        "Explain Redis semantic caching functionality"
    ]

    for i, query in enumerate(queries, 1):
        print(f"🔍 Query {i}: '{query}'")
        start_time = time.time()

        try:
            result = get_cached_or_generate(query)
            query_time = time.time() - start_time
            print(f"⏱️  Time taken: {query_time:.2f} seconds")
            print(f"📝 Response: {result[:100]}{'...' if len(result) > 100 else ''}\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")

        # Small delay between queries
        if i < len(queries):
            time.sleep(0.5)

if __name__ == "__main__":
    try:
        # Run the main caching demo
        demo_semantic_caching()

        # Run the semantic similarity demo
        demo_similar_queries()

    except KeyboardInterrupt:
        print("\n\n🛑 Demo interrupted by user")
    except Exception as e:
        print(f"\n❌ Demo failed with error: {e}")
        print("💡 Make sure your .env file contains the correct RDS_URI")
