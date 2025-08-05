# 🔍 RAG-Anything Multi-Modal Parser

A Streamlit application demonstrating RAG-Anything's multi-modal content parsing capabilities. Parse documents and extract structured content from PDFs, DOCX, Excel files, images, and more.

![RAG Parser Demo](https://img.shields.io/badge/Status-Ready-green) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)

## ✨ Features

- 📄 **PDF Parsing**: Extract text, images, and tables from PDF documents
- 📝 **DOCX Processing**: Parse Word documents with full formatting preservation  
- 📊 **Excel Analysis**: Extract data from spreadsheets with structure detection
- 🖼️ **Image OCR**: Text extraction from images using Tesseract
- 📋 **Multi-Format Output**: Results in both JSON and Markdown formats
- 🎯 **Content Classification**: Automatic categorization of text blocks, headers, lists
- 📈 **Statistics Dashboard**: Comprehensive parsing metrics and visualizations

## 🚀 Quick Start

### One-Command Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/rag-anything-demo.git
cd rag-anything-demo

# Setup everything (dependencies, virtual environment, system packages)
chmod +x setup.sh && ./setup.sh

# Start the application
./run.sh
```

That's it! The app will open in your browser at `http://localhost:8501`

### Manual Setup (if needed)

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install system dependencies
# macOS:
brew install tesseract poppler

# Linux (Ubuntu/Debian):
sudo apt-get install tesseract-ocr poppler-utils

# Start the app
streamlit run app.py
```

## 📋 Requirements

### System Requirements
- **Python 3.8+**
- **System packages**: tesseract-ocr, poppler-utils
- **OS**: macOS, Linux, Windows (with WSL recommended)

### Python Dependencies
- streamlit >= 1.28.0
- PyPDF2 >= 3.0.0
- python-docx >= 0.8.11
- openpyxl >= 3.1.0
- pytesseract >= 0.3.10
- opencv-python-headless >= 4.8.0
- Pillow >= 10.0.0

See `requirements.txt` for the complete list.

## 🎯 Usage

1. **Start the application**: `./run.sh`
2. **Upload a document**: PDF, DOCX, Excel, image, or text file
3. **View parsing results**: 
   - Real-time content extraction
   - Statistics and metrics
   - Structured data visualization
4. **Export results**: Download as JSON or Markdown

### Supported File Types

| Format | Extension | Features |
|--------|-----------|----------|
| PDF | `.pdf` | Text extraction, image detection, table parsing |
| Word | `.docx` | Paragraph extraction, table parsing, formatting |
| Excel | `.xlsx`, `.xls` | Sheet parsing, data extraction, structure detection |
| Images | `.png`, `.jpg`, `.jpeg` | OCR text extraction, metadata analysis |
| Text | `.txt`, `.md` | Content classification, structure analysis |

## 🏗️ Architecture

```
RAG-Anything Parser
├── 🎨 Frontend (Streamlit)
├── 🧠 Content Parser (Multi-modal)
│   ├── PDF Parser (PyPDF2)
│   ├── DOCX Parser (python-docx)
│   ├── Excel Parser (openpyxl)
│   ├── Image Parser (PIL + Tesseract)
│   └── Text Parser (Built-in)
├── 📊 Output Formatter (JSON/Markdown)
└── 🔧 Utilities (File handling, metrics)
```

## 🛠️ Development

### Project Structure
```
rag-anything-demo/
├── app.py              # Main Streamlit application
├── utils.py            # Core parsing utilities
├── config.py           # Configuration management
├── requirements.txt    # Python dependencies
├── packages.txt        # System dependencies (for cloud)
├── setup.sh           # One-command setup script
├── run.sh             # Quick start script
└── .streamlit/
    └── config.toml    # Streamlit configuration
```

### Local Development
```bash
# Activate environment
source venv/bin/activate

# Install additional development dependencies
pip install lightrag --pre  # Latest RAG libraries

# Run in development mode
streamlit run app.py --logger.level=debug
```

## ☁️ Cloud Deployment

### Streamlit Cloud
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy with `app.py` as the main file

The `packages.txt` file ensures system dependencies (tesseract, poppler) are installed automatically.

### Other Platforms
- **Heroku**: See `DEPLOYMENT.md` for detailed instructions
- **Docker**: Use the provided Dockerfile
- **Railway**: One-click deployment from GitHub

## 📊 Performance

- **File Size Limit**: 200MB (configurable)
- **Processing Speed**: 
  - Small PDFs (< 10 pages): ~2-5 seconds
  - Large documents: ~10-30 seconds
  - Images with OCR: ~5-15 seconds
- **Memory Usage**: ~100-500MB depending on document size

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test locally: `./run.sh`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues

**OCR not working**
```bash
# macOS
brew install tesseract

# Linux
sudo apt-get install tesseract-ocr tesseract-ocr-eng
```

**Import errors**
```bash
# Reinstall dependencies
source venv/bin/activate
pip install -r requirements.txt --force-reinstall
```

**Permission denied**
```bash
chmod +x setup.sh run.sh
```

### Getting Help
- 📚 Check the [DEPLOYMENT.md](DEPLOYMENT.md) for detailed setup instructions
- 🐛 Report issues on GitHub
- 💬 Ask questions in the Issues section

## 🌟 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Document parsing powered by PyPDF2, python-docx, openpyxl
- OCR functionality using [Tesseract](https://github.com/tesseract-ocr/tesseract)
- RAG architecture inspired by modern multi-modal parsing techniques

---

**Happy Parsing!** 🚀📚