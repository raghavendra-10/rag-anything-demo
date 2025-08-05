# Installing RAG-Anything for Full Functionality

This guide will help you install the actual RAG-Anything library to replace the mock parser with real multi-modal parsing capabilities.

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for GitHub installations)
- 4GB+ RAM recommended
- CUDA-compatible GPU (optional, for faster processing)

## 🚀 Installation Options

### Option 1: Install from PyPI (Recommended)

```bash
# Install core RAG-Anything
pip install raganything

# Install additional dependencies
pip install lightrag magic-pdf mineru
```

### Option 2: Install from GitHub (Latest)

```bash
# Install from GitHub repository
pip install git+https://github.com/lightrag-ai/lightrag.git

# Or clone and install locally
git clone https://github.com/lightrag-ai/lightrag.git
cd lightrag
pip install -e .
```

### Option 3: Install with All Dependencies

```bash
# Update requirements and install everything
pip install -r requirements.txt

# Additional ML dependencies for enhanced functionality
pip install torch torchvision torchaudio
pip install transformers sentence-transformers
pip install pytesseract opencv-python
```

## 🔧 System Dependencies

### macOS
```bash
# Install system dependencies
brew install tesseract
brew install poppler  # For PDF processing
```

### Ubuntu/Debian
```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install poppler-utils
sudo apt-get install python3-opencv
```

### Windows
```bash
# Install via conda (recommended for Windows)
conda install -c conda-forge tesseract
conda install -c conda-forge poppler
```

## 🧪 Verify Installation

Run this test to verify RAG-Anything is working:

```bash
python -c "
try:
    from raganything import RAGAnything, RAGAnythingConfig
    print('✅ RAG-Anything installed successfully')
except ImportError as e:
    print(f'❌ RAG-Anything not found: {e}')
    try:
        from lightrag import LightRAG
        print('✅ LightRAG available as fallback')
    except ImportError:
        print('❌ No RAG libraries found')
"
```

## 🔑 API Keys (Optional)

For enhanced functionality, you may need API keys:

```bash
# Set environment variables (optional)
export OPENAI_API_KEY="your-openai-key"
export HUGGINGFACE_API_KEY="your-hf-key"
```

Or create a `.env` file:
```env
OPENAI_API_KEY=your-openai-key
HUGGINGFACE_API_KEY=your-hf-key
```

## 🚀 Test with Real Parser

After installation, restart the Streamlit app:

```bash
streamlit run app.py
```

You should see:
- ✅ Parser ready for document processing
- 🚀 Using RAG-Anything real parser (instead of demonstration parser)
- Enhanced parsing results with higher confidence scores

## 📊 Expected Improvements

With the real RAG-Anything library, you'll get:

| Feature | Mock Parser | Real RAG-Anything |
|---------|-------------|-------------------|
| **Accuracy** | Demo data | Real extraction |
| **Confidence** | Fixed scores | Dynamic confidence |
| **Content Types** | Basic simulation | Full multi-modal |
| **File Support** | Limited | Comprehensive |
| **Processing** | Instant | Real parsing time |
| **Embeddings** | Not available | Vector-ready |

## 🐛 Troubleshooting

### Installation Issues

**Problem**: `pip install raganything` fails
```bash
# Try alternative installation
pip install --upgrade pip
pip install wheel setuptools
pip install raganything --no-cache-dir
```

**Problem**: CUDA/GPU issues
```bash
# Install CPU-only version
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

**Problem**: System dependencies missing
```bash
# Check system dependencies
tesseract --version
python -c "import cv2; print(cv2.__version__)"
```

### Runtime Issues

**Problem**: "Parser initialization failed"
- Check that all dependencies are installed
- Verify system dependencies (tesseract, poppler)
- Check available memory (4GB+ recommended)

**Problem**: Slow parsing performance
- Enable GPU acceleration if available
- Reduce file sizes for testing
- Check system resources

## 📈 Performance Optimization

### For Better Performance:

1. **GPU Acceleration**:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

2. **Memory Optimization**:
   ```python
   # In your config
   config.processing.chunk_size = 500  # Smaller chunks
   config.processing.max_file_size_mb = 25  # Smaller files
   ```

3. **Parallel Processing**:
   - Process multiple documents in batches
   - Use multiprocessing for large files

## 🔄 Switching Back to Mock Parser

If you want to switch back to the demonstration parser:

```python
# In utils.py, force mock parser
RAG_AVAILABLE = False
```

Or uninstall RAG-Anything:
```bash
pip uninstall raganything lightrag
```

## 📞 Support

- **RAG-Anything Issues**: [GitHub Issues](https://github.com/raganything/raganything/issues)
- **LightRAG Issues**: [GitHub Issues](https://github.com/lightrag-ai/lightrag/issues)
- **Demo App Issues**: Check the main README.md

---

**Ready to test real multi-modal parsing!** 🚀

Once installed, upload your documents to see the difference between mock parsing and real RAG-Anything extraction capabilities.