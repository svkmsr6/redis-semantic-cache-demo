#!/bin/bash

echo "🚀 Starting Redis Semantic Cache Demo on Replit"
echo "================================================"

# Check if environment variables are set
if [ -z "$RDS_URI" ]; then
    echo "❌ Warning: RDS_URI not set in Replit Secrets"
    echo "   Please add your Redis connection string to Secrets"
fi

if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ Warning: OPENAI_API_KEY not set in Replit Secrets"
    echo "   Please add your OpenAI API key to Secrets"
fi

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "🌐 Starting Flask application..."
python app.py
