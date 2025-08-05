#!/bin/bash

# RAG-Anything Parser - Auto Setup & Run
echo "🚀 RAG-Anything Multi-Modal Parser"
echo "=================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3.8+ and try again."
    exit 1
fi

# Auto-setup if virtual environment doesn't exist
if [ ! -d "venv" ]; then
    echo "🔧 First time setup - Creating virtual environment..."
    python3 -m venv venv
    
    echo "📦 Installing dependencies..."
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    
    echo "🧪 Checking system dependencies..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if ! command -v tesseract &> /dev/null; then
            echo "⚠️ Tesseract not found. Install with: brew install tesseract poppler"
        fi
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        if ! command -v tesseract &> /dev/null; then
            echo "⚠️ Tesseract not found. Install with: sudo apt-get install tesseract-ocr poppler-utils"
        fi
    fi
    
    echo "✅ Setup complete!"
else
    # Activate existing environment
    source venv/bin/activate
fi

# Check if streamlit is installed
if ! command -v streamlit &> /dev/null; then
    echo "📦 Installing missing dependencies..."
    pip install -r requirements.txt
fi

# Start the application
echo ""
echo "🌟 Starting RAG-Anything Parser..."
echo "📍 URL: http://localhost:8501"
echo ""
echo "💡 Usage Tips:"
echo "   - Upload PDF, DOCX, Excel, or image files"
echo "   - View results in JSON or Markdown format"
echo "   - Press Ctrl+C to stop the server"
echo ""

streamlit run app.py