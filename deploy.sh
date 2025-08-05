#!/bin/bash

# RAG-Anything Parser Deployment Script
echo "🚀 RAG-Anything Parser Deployment"
echo "=================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial RAG-Anything parser implementation"
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already exists"
fi

# Check current directory
echo "📍 Current directory: $(pwd)"
echo "📂 Files ready for deployment:"
ls -la

echo ""
echo "🔍 Deployment Checklist:"
echo "========================"

# Check required files
files=(
    "app.py"
    "requirements.txt" 
    "packages.txt"
    ".streamlit/config.toml"
    "DEPLOYMENT.md"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ $file (missing)"
    fi
done

echo ""
echo "🚀 Deployment Options:"
echo "======================"
echo "1. Streamlit Cloud (Recommended):"
echo "   - Push to GitHub: git remote add origin https://github.com/yourusername/rag-anything-demo.git"
echo "   - Push code: git push -u origin main"
echo "   - Deploy: https://share.streamlit.io"
echo ""
echo "2. Local Testing:"
echo "   - Run: streamlit run app.py"
echo ""
echo "3. Docker:"
echo "   - Build: docker build -t rag-parser ."
echo "   - Run: docker run -p 8501:8501 rag-parser"
echo ""

# Test dependencies
echo "🧪 Testing Dependencies:"
echo "========================"
python3 -c "
try:
    import streamlit
    print('✅ Streamlit')
except: print('❌ Streamlit')

try:
    import lightrag
    print('✅ LightRAG')
except: print('❌ LightRAG')
    
try:
    import PyPDF2
    print('✅ PyPDF2')
except: print('❌ PyPDF2')

try:
    from docx import Document
    print('✅ python-docx')
except: print('❌ python-docx')
"

echo ""
echo "🎯 Ready for deployment!"
echo "📖 See DEPLOYMENT.md for detailed instructions"