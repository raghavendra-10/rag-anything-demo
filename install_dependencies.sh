#!/bin/bash

# RAG-Anything Demo Installation Script
# This script installs all required dependencies for real RAG parsing

echo "🚀 Installing RAG-Anything Demo Dependencies"
echo "============================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not found. Please install Python 3.8+"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install core dependencies first
echo "📚 Installing core dependencies..."
pip install streamlit pandas numpy

# Install document processing libraries
echo "📄 Installing document processing libraries..."
pip install python-docx openpyxl PyPDF2 Pillow python-magic
pip install markdown beautifulsoup4

# Install RAG libraries
echo "🧠 Installing RAG libraries..."
pip install lightrag

# Try to install additional RAG components
echo "🔍 Installing additional parsing libraries..."
pip install magic-pdf || echo "⚠️ magic-pdf not available, skipping..."
pip install mineru || echo "⚠️ mineru not available, skipping..."

# Install OCR capabilities
echo "👁️ Installing OCR libraries..."
pip install pytesseract opencv-python

# Install ML libraries (optional but recommended)
echo "🤖 Installing ML libraries..."
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install transformers sentence-transformers

echo ""
echo "🎉 Installation completed!"
echo ""
echo "📋 Installation Summary:"
echo "========================"

# Check what was installed successfully
echo "Core libraries:"
python3 -c "
try:
    import streamlit; print('✅ Streamlit')
except: print('❌ Streamlit')
try:
    import pandas; print('✅ Pandas')
except: print('❌ Pandas')
"

echo "Document processing:"
python3 -c "
try:
    import docx; print('✅ python-docx')
except: print('❌ python-docx')
try:
    import openpyxl; print('✅ openpyxl')
except: print('❌ openpyxl')
try:
    import PyPDF2; print('✅ PyPDF2')
except: print('❌ PyPDF2')
try:
    from PIL import Image; print('✅ Pillow')
except: print('❌ Pillow')
"

echo "RAG libraries:"
python3 -c "
try:
    from lightrag import LightRAG; print('✅ LightRAG')
except: print('❌ LightRAG')
try:
    import magic_pdf; print('✅ magic-pdf')
except: print('⚠️ magic-pdf (optional)')
try:
    import mineru; print('✅ mineru')
except: print('⚠️ mineru (optional)')
"

echo "OCR capabilities:"
python3 -c "
try:
    import pytesseract; print('✅ pytesseract')
except: print('❌ pytesseract')
try:
    import cv2; print('✅ opencv-python')
except: print('❌ opencv-python')
"

echo ""
echo "🚀 To run the application:"
echo "========================="
echo "source venv/bin/activate"
echo "streamlit run app.py"
echo ""

# Check for system dependencies
echo "🔍 System Dependencies Check:"
echo "============================"

if command -v tesseract &> /dev/null; then
    echo "✅ Tesseract OCR: $(tesseract --version | head -n1)"
else
    echo "⚠️ Tesseract OCR not found. Install with:"
    echo "   macOS: brew install tesseract"
    echo "   Ubuntu: sudo apt-get install tesseract-ocr"
fi

if command -v poppler-utils &> /dev/null || command -v pdftoppm &> /dev/null; then
    echo "✅ Poppler utilities available"
else
    echo "⚠️ Poppler utilities not found. Install with:"
    echo "   macOS: brew install poppler"
    echo "   Ubuntu: sudo apt-get install poppler-utils"
fi

echo ""
echo "🎯 Ready to parse documents with real RAG-Anything!"