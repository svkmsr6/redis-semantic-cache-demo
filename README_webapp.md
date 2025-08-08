# Redis Semantic Cache Web Demo

A Flask web application that replicates the functionality of `demo_search.py` with an interactive frontend interface.

## Features

- **Single Query Testing**: Execute individual queries and see caching behavior
- **Semantic Caching Demo**: Run the same query twice to demonstrate cache performance
- **Similarity Demo**: Test semantically similar queries to showcase cache effectiveness
- **Real-time Performance Metrics**: View query timing, cache hit/miss status, and speedup calculations
- **Query History**: Track all executed queries with timestamps and performance data
- **API Status Monitoring**: Check OpenAI API connectivity and quota status

## Setup

1. Ensure your `.env` file contains:
   ```
   RDS_URI=your_redis_connection_string
   OPENAI_API_KEY=your_openai_api_key
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the web application:
   ```bash
   python app.py
   ```

4. Open your browser to: `http://localhost:5000`

## API Endpoints

- `GET /` - Main web interface
- `GET /api/status` - Check OpenAI API status
- `POST /api/query` - Execute a single query
- `POST /api/demo/caching` - Run caching demonstration
- `POST /api/demo/similarity` - Run similarity demonstration
- `GET /api/history` - Get query history
- `POST /api/history/clear` - Clear query history

## Usage

### Single Query
Enter any query in the "Single Query" card and click "Execute Query" to test individual queries.

### Caching Demo
This replicates the main functionality from `demo_search.py`:
1. Enter a query (or use the default)
2. Click "Run Caching Demo"
3. The system will execute the same query twice
4. View performance metrics showing cache effectiveness

### Similarity Demo
Tests semantically similar queries:
1. Click "Run Similarity Demo" for default similar queries
2. Or click "Custom Queries" to enter your own similar queries
3. View how semantic similarity affects caching

## Performance Metrics

The web app displays:
- **Query Time**: Execution time for each query
- **Cache Status**: Whether the query was a cache hit or miss
- **Speedup**: Performance improvement from caching
- **Time Saved**: Actual time saved by cache hits

## Troubleshooting

- **API Status Red**: Check your OpenAI API key and billing
- **No Cache Hits**: Verify Redis connection string in `.env`
- **Slow Queries**: Normal for first-time queries; subsequent should be faster
