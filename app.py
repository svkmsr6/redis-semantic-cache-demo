"""
Flask Web Application for Redis Semantic Caching Demo
Replicates the functionality of demo_search.py with a web interface
"""
import time
from flask import Flask, render_template, request, jsonify
from rsearch_module import get_cached_or_generate, check_openai_status

app = Flask(__name__)

# Store query history for the session
query_history = []

@app.route('/')
def index():
    """Main page with the demo interface"""
    return render_template('index.html')

@app.route('/api/status')
def api_status():
    """Check OpenAI API status"""
    try:
        status = check_openai_status()
        return jsonify(status)
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Status check failed: {str(e)}"
        })

@app.route('/api/query', methods=['POST'])
def api_query():
    """Process a single query and return results with timing"""
    try:
        data = request.get_json()
        query = data.get('query', '').strip()
        
        if not query:
            return jsonify({
                "status": "error",
                "message": "Query cannot be empty"
            }), 400
        
        # Record start time
        start_time = time.time()
        
        # Execute the query
        try:
            result = get_cached_or_generate(query)
            query_time = time.time() - start_time
            
            # Determine if it was likely a cache hit (very fast response)
            is_cache_hit = query_time < 0.5  # Less than 500ms suggests cache hit
            
            # Add to history
            query_entry = {
                "id": len(query_history) + 1,
                "query": query,
                "result": result,
                "time": query_time,
                "is_cache_hit": is_cache_hit,
                "timestamp": time.strftime("%H:%M:%S")
            }
            query_history.append(query_entry)
            
            return jsonify({
                "status": "success",
                "data": query_entry
            })
            
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": f"Query execution failed: {str(e)}"
            }), 500
            
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Request processing failed: {str(e)}"
        }), 500

@app.route('/api/demo/caching', methods=['POST'])
def api_demo_caching():
    """Run the semantic caching demo (same query twice)"""
    try:
        data = request.get_json()
        test_query = data.get('query', 'What is semantic caching in Redis Cloud?')
        
        results = []
        
        # First query - should be cache miss
        print("Running first query (cache miss expected)...")
        start_time = time.time()
        try:
            result1 = get_cached_or_generate(test_query)
            first_time = time.time() - start_time
            
            first_entry = {
                "query_number": 1,
                "query": test_query,
                "result": result1,
                "time": first_time,
                "is_cache_hit": False,
                "timestamp": time.strftime("%H:%M:%S")
            }
            results.append(first_entry)
            
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": f"First query failed: {str(e)}"
            }), 500
        
        # Small delay
        time.sleep(1)
        
        # Second query - should be cache hit
        print("Running second query (cache hit expected)...")
        start_time = time.time()
        try:
            result2 = get_cached_or_generate(test_query)
            second_time = time.time() - start_time
            
            second_entry = {
                "query_number": 2,
                "query": test_query,
                "result": result2,
                "time": second_time,
                "is_cache_hit": second_time < first_time * 0.5,  # Much faster = cache hit
                "timestamp": time.strftime("%H:%M:%S")
            }
            results.append(second_entry)
            
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": f"Second query failed: {str(e)}"
            }), 500
        
        # Calculate performance metrics
        speedup = first_time / second_time if second_time > 0 else 0
        time_saved = first_time - second_time
        
        performance = {
            "first_time": first_time,
            "second_time": second_time,
            "speedup": speedup,
            "time_saved": time_saved,
            "significant_speedup": speedup > 2.0
        }
        
        # Add to history
        for entry in results:
            entry["id"] = len(query_history) + 1
            query_history.append(entry)
        
        return jsonify({
            "status": "success",
            "data": {
                "results": results,
                "performance": performance
            }
        })
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Caching demo failed: {str(e)}"
        }), 500

@app.route('/api/demo/similarity', methods=['POST'])
def api_demo_similarity():
    """Run the semantic similarity demo with multiple related queries"""
    try:
        # Default similar queries
        default_queries = [
            "How does Redis semantic cache work?",
            "What is the mechanism behind Redis semantic caching?",
            "Explain Redis semantic caching functionality"
        ]
        
        data = request.get_json()
        queries = data.get('queries', default_queries)
        
        if not isinstance(queries, list) or len(queries) == 0:
            return jsonify({
                "status": "error",
                "message": "Queries must be a non-empty list"
            }), 400
        
        results = []
        
        for i, query in enumerate(queries, 1):
            print(f"Running similarity query {i}: {query}")
            start_time = time.time()
            
            try:
                result = get_cached_or_generate(query)
                query_time = time.time() - start_time
                
                entry = {
                    "query_number": i,
                    "query": query,
                    "result": result,
                    "time": query_time,
                    "is_cache_hit": query_time < 0.5,
                    "timestamp": time.strftime("%H:%M:%S")
                }
                results.append(entry)
                
                # Add to history
                entry["id"] = len(query_history) + 1
                query_history.append(entry)
                
                # Small delay between queries
                if i < len(queries):
                    time.sleep(0.5)
                    
            except Exception as e:
                return jsonify({
                    "status": "error",
                    "message": f"Query {i} failed: {str(e)}"
                }), 500
        
        return jsonify({
            "status": "success",
            "data": {
                "results": results,
                "total_queries": len(queries)
            }
        })
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Similarity demo failed: {str(e)}"
        }), 500

@app.route('/api/history')
def api_history():
    """Get query history"""
    return jsonify({
        "status": "success",
        "data": query_history
    })

@app.route('/api/history/clear', methods=['POST'])
def api_clear_history():
    """Clear query history"""
    global query_history
    query_history = []
    return jsonify({
        "status": "success",
        "message": "History cleared"
    })

if __name__ == '__main__':
    print("🚀 Starting Redis Semantic Cache Web Demo")
    print("📁 Make sure your .env file contains RDS_URI and OPENAI_API_KEY")
    print("🌐 Open http://localhost:5000 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5000)
