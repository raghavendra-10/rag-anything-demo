#!/bin/bash

# RAG-Anything Parser - One Command Setup
echo "🚀 Setting up RAG-Anything Multi-Modal Parser..."
echo "================================================"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3.8+ and try again."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Found Python $python_version"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install system dependencies based on OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    echo "🍎 Detected macOS - Installing system dependencies..."
    if command -v brew &> /dev/null; then
        brew install tesseract poppler
        echo "✅ Installed tesseract and poppler via Homebrew"
    else
        echo "⚠️ Homebrew not found. Please install:"
        echo "   brew install tesseract poppler"
    fi
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    echo "🐧 Detected Linux - Installing system dependencies..."
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y tesseract-ocr tesseract-ocr-eng poppler-utils libmagic1
        echo "✅ Installed system dependencies via apt-get"
    elif command -v yum &> /dev/null; then
        sudo yum install -y tesseract poppler-utils file
        echo "✅ Installed system dependencies via yum"
    else
        echo "⚠️ Please install manually:"
        echo "   tesseract-ocr poppler-utils"
    fi
else
    echo "⚠️ Unknown OS. Please install manually:"
    echo "   - tesseract-ocr"
    echo "   - poppler-utils"
fi

# Install Python dependencies
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

# Install additional RAG libraries for full functionality
echo "🧠 Installing additional RAG libraries..."
pip install lightrag --pre || echo "⚠️ LightRAG installation failed (beta version may be unstable)"

# Test installation
echo "🧪 Testing installation..."
python3 -c "
import streamlit
import pandas
import PyPDF2
from docx import Document
import openpyxl
from PIL import Image
try:
    import pytesseract
    pytesseract.get_tesseract_version()
    print('✅ All core libraries imported successfully')
    print('✅ OCR (tesseract) is working')
except:
    print('⚠️ OCR (tesseract) may not be available')
"

# Create run script
echo "📝 Creating run script..."
cat > run.sh << 'EOF'
#!/bin/bash
echo "🚀 Starting RAG-Anything Multi-Modal Parser..."
source venv/bin/activate
streamlit run app.py
EOF

chmod +x run.sh

# Create requirements for full local setup
echo "📋 Creating local requirements file..."
cat > requirements-full.txt << 'EOF'
# Full local setup with all RAG-Anything capabilities
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
python-docx>=0.8.11
openpyxl>=3.1.0
PyPDF2>=3.0.0
Pillow>=10.0.0
markdown>=3.5.0
beautifulsoup4>=4.12.0
pytesseract>=0.3.10
opencv-python-headless>=4.8.0

# RAG libraries (install with --pre for beta versions)
lightrag>=0.1.0b6

# Optional: Full ML stack (requires more resources)
# torch>=2.0.0
# transformers>=4.30.0
EOF

echo ""
echo "🎉 Setup Complete!"
echo "=================="
echo ""
echo "📁 Files created:"
echo "   - venv/          Virtual environment"
echo "   - run.sh         Start the application"
echo "   - requirements-full.txt   Full local requirements"
echo ""
echo "🚀 To start the app:"
echo "   ./run.sh"
echo ""
echo "🔧 To activate environment manually:"
echo "   source venv/bin/activate"
echo ""
echo "📚 To install full ML stack later:"
echo "   source venv/bin/activate"
echo "   pip install torch transformers"
echo ""