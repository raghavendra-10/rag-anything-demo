#!/bin/bash

# RAG-Anything Parser - Quick Start
echo "🚀 Starting RAG-Anything Multi-Modal Parser..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run setup first: ./setup.sh"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit not found in virtual environment"
    echo "Please run setup first: ./setup.sh"
    exit 1
fi

# Start the application
echo "🌟 Opening RAG-Anything Parser in your browser..."
echo "📍 URL: http://localhost:8501"
echo ""
echo "💡 Tips:"
echo "   - Upload PDF, DOCX, Excel, or image files"
echo "   - View results in JSON or Markdown format"
echo "   - Press Ctrl+C to stop the server"
echo ""

streamlit run app.py