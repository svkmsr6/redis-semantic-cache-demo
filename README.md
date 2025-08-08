# Redis Semantic Cache Demo

A comprehensive web application demonstrating semantic caching capabilities using Redis Cloud and OpenAI, replicating and enhancing the functionality of the original `demo_search.py` script.

## 🚀 Features

- **Interactive Web Interface**: Beautiful, responsive UI built with Bootstrap and Font Awesome
- **Single Query Testing**: Execute individual queries and observe caching behavior
- **Semantic Caching Demo**: Run identical queries twice to demonstrate cache performance
- **Similarity Demo**: Test semantically similar queries to showcase cache effectiveness
- **Real-time Performance Metrics**: View query timing, cache hit/miss status, and speedup calculations
- **Query History**: Track all executed queries with timestamps and performance data
- **API Status Monitoring**: Real-time OpenAI API connectivity and quota status checking
- **Accordion Interface**: Clean, collapsible response display with proper formatting

## 📋 Prerequisites

- Python 3.8+
- Redis Cloud account and connection string
- OpenAI API key
- Virtual environment (recommended)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/svkmsr6/redis-semantic-cache.git
   cd redis-semantic-cache
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv redis-searchenv
   # On Windows:
   redis-searchenv\Scripts\activate
   # On macOS/Linux:
   source redis-searchenv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```env
   RDS_URI=your_redis_connection_string
   OPENAI_API_KEY=your_openai_api_key
   ```

## 🚀 Quick Start

### Web Application
```bash
python app.py
```
Then open your browser to: `http://localhost:5000`

### Command Line Demo
```bash
python demo_search.py
```

### Convenience Scripts
- **Windows**: Double-click `start_webapp.bat` or run `start_webapp.ps1`
- **Cross-platform**: Use the VS Code task "Run Redis Semantic Cache Web App"

## 📱 Web Interface

The web application provides three main demonstration modes:

### 1. Single Query
- Enter any query to test individual caching behavior
- See real-time performance metrics
- View cache hit/miss status

### 2. Caching Demo
- Executes the same query twice
- Demonstrates cache performance improvement
- Shows detailed performance analysis with speedup calculations

### 3. Similarity Demo
- Tests semantically similar queries
- Choose from default queries or create custom ones
- Observe how semantic similarity affects caching

## 🏗️ Project Structure

```
redis-semantic-cache/
├── app.py                      # Flask web application
├── demo_search.py             # Original command-line demo
├── rsearch_module/            # Core semantic search functionality
│   └── __init__.py
├── templates/
│   └── index.html            # Web interface template
├── static/
│   └── style.css            # Custom styling
├── requirements.txt          # Python dependencies
├── start_webapp.bat         # Windows launcher
├── start_webapp.ps1         # PowerShell launcher
├── README_webapp.md         # Web app specific documentation
└── .env                     # Environment variables (create this)
```

## 🔧 API Endpoints

The Flask application exposes several REST endpoints:

- `GET /` - Main web interface
- `GET /api/status` - Check OpenAI API status
- `POST /api/query` - Execute a single query
- `POST /api/demo/caching` - Run caching demonstration
- `POST /api/demo/similarity` - Run similarity demonstration
- `GET /api/history` - Get query history
- `POST /api/history/clear` - Clear query history

## 📊 Performance Features

The application tracks and displays:
- **Query Execution Time**: Precise timing for each query
- **Cache Hit/Miss Status**: Visual indicators for cache effectiveness
- **Performance Speedup**: Calculated improvement from caching
- **Time Saved**: Actual time savings from cache hits

## 🎨 User Interface

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Accordion Responses**: Clean, collapsible display of AI responses
- **Real-time Status**: Live API connectivity monitoring
- **Performance Metrics**: Visual charts and indicators
- **Query History**: Persistent session history with timestamps

## 🔍 Core Technologies

- **Backend**: Flask, OpenAI API, Redis
- **Frontend**: Bootstrap 5, Font Awesome, Vanilla JavaScript
- **Caching**: Redis Vector Library (redisvl) with semantic cache
- **Embeddings**: Sentence Transformers (all-mpnet-base-v2)
- **AI Model**: OpenAI GPT-4o-mini

## 🚨 Troubleshooting

### Common Issues

1. **API Status Red**: 
   - Check your OpenAI API key in `.env`
   - Verify billing status at OpenAI dashboard

2. **No Cache Hits**: 
   - Verify Redis connection string
   - Check Redis Cloud connectivity

3. **Slow Initial Queries**: 
   - Normal behavior for first-time queries
   - Subsequent similar queries should be faster

4. **Module Import Errors**:
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt`

### Error Messages

- `QUOTA_EXCEEDED`: Check OpenAI billing and usage limits
- `AUTH_ERROR`: Verify OpenAI API key is correct
- `RATE_LIMITED`: Wait and retry, or upgrade OpenAI plan

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Redis for powerful caching capabilities
- OpenAI for advanced language models
- Bootstrap team for excellent UI framework
- Sentence Transformers for embedding models

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the [issues](https://github.com/svkmsr6/redis-semantic-cache/issues) page
3. Create a new issue with detailed information

---

**Made with ❤️ for the Redis and AI community**
