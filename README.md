# RAG-Anything Multi-Modal Parser

A production-ready Streamlit application using **real RAG-Anything libraries** for multi-modal content parsing. This application demonstrates actual document processing capabilities using LightRAG and associated parsing libraries for comprehensive content extraction.

![RAG-Anything Demo](https://img.shields.io/badge/Streamlit-Parser%20Demo-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Focus](https://img.shields.io/badge/Focus-Parsing%20Architecture-orange)

## 🎯 Focus: Pure Parsing Architecture Testing

This demo is specifically designed to test and demonstrate:
- **Multi-modal content parsing** without LLM dependencies
- **RAG-Anything architecture** validation
- **Content extraction capabilities** across different file types
- **Parsing accuracy and structure** analysis
- **Output formats** (JSON and Markdown) for integration testing

## 🌟 Key Features

### Core Parsing Capabilities
- **📝 Text Extraction**: Hierarchical text blocks with content classification
- **🖼️ Image Processing**: Caption extraction and metadata analysis
- **📊 Table Parsing**: Structure detection with confidence scores
- **🧮 Equation Recognition**: LaTeX equation extraction and rendering
- **🔍 Content Classification**: Automatic categorization of content types

### Testing & Analysis Tools
- **Real-time Parsing**: Live document processing with progress indicators
- **Confidence Scoring**: Parser confidence levels for each extracted element
- **Content Metrics**: Detailed statistics on parsing results
- **Multiple Output Formats**: JSON and Markdown for different use cases
- **Architecture Validation**: See exactly how RAG-Anything processes content

### User Interface
- **Parser Configuration**: Toggle different processing modes
- **Content Inspection**: Detailed view of extracted elements
- **Comparison Tools**: Side-by-side JSON and Markdown output
- **Download Options**: Export parsing results for further analysis

## 📋 Requirements

- Python 3.8 or higher
- RAG-Anything library (or mock fallback for testing)
- 1GB+ RAM for document processing
- No LLM API keys required!

## 🚀 Quick Start

### 1. Automated Installation (Recommended)

```bash
# Navigate to project directory
cd rag-anything-demo

# Run the installation script
./install_dependencies.sh
```

### 2. Manual Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install core RAG libraries
pip install lightrag magic-pdf mineru

# Install all dependencies
pip install -r requirements.txt

# Install system dependencies (macOS)
brew install tesseract poppler
```

### 3. Run the Application

```bash
# Activate environment (if not already active)
source venv/bin/activate

# Start the application
streamlit run app.py
```

The application will open at `http://localhost:8501`

### 3. Test Parsing Architecture

1. **Initialize Parser**: Click "Initialize RAG-Anything Parser" in sidebar
2. **Configure Processing**: Toggle image, table, and equation processing
3. **Upload Document**: Test with PDF, DOCX, PPTX, XLSX, images, or text files
4. **Analyze Results**: Explore parsed content in tabbed interface
5. **Export Results**: Download JSON or Markdown outputs

## 📖 Usage Guide

### Testing Workflow

1. **Parser Configuration**:
   - Enable/disable specific content types (images, tables, equations)
   - Choose parser type (auto/mineru)
   - Select output formats (JSON, Markdown, or both)

2. **Document Upload**:
   - Drag-and-drop or browse for files
   - Supported: PDF, DOCX, PPTX, XLSX, PNG, JPG, TXT, MD
   - Maximum file size: 50MB

3. **Parsing Analysis**:
   - View real-time processing progress
   - Examine confidence scores for each element
   - Compare different content type extractions

4. **Result Inspection**:
   - **Text Tab**: See hierarchical text extraction with classifications
   - **Images Tab**: Review image captions and metadata
   - **Tables Tab**: Analyze table structure and content parsing
   - **Equations Tab**: Check LaTeX equation recognition
   - **JSON Tab**: Complete parsing results in JSON format
   - **Markdown Tab**: Human-readable formatted output

### Content Analysis Features

| Content Type | Analysis Features |
|--------------|-------------------|
| **📝 Text** | Type classification, word count, confidence scores, line numbers |
| **🖼️ Images** | Caption extraction, metadata analysis, text recognition |
| **📊 Tables** | Header detection, row/column parsing, data type analysis |
| **🧮 Equations** | LaTeX conversion, variable identification, context analysis |

## 🛠️ Technical Architecture

```
rag-anything-demo/
├── app.py              # Main Streamlit parsing interface
├── config.py           # Parser configuration management
├── utils.py            # Content processing and formatting utilities
├── requirements.txt    # Minimal dependencies (no LLM required)
└── README.md          # This documentation
```

### Key Components

- **`ContentParser`**: RAG-Anything integration with fallback mock parser
- **`OutputFormatter`**: JSON and Markdown result formatting
- **`MockRAGParser`**: Demonstration parser when RAG-Anything unavailable
- **Configuration System**: Flexible parsing options and output formats

### Dependencies (Simplified)

```
streamlit              # Web interface
raganything           # Core parsing library
pandas                # Data handling
python-docx           # Word document support
openpyxl              # Excel file support
PyPDF2                # PDF processing
Pillow                # Image processing
markdown              # Markdown formatting
beautifulsoup4        # HTML/text processing
```

## 📊 Parsing Output Examples

### JSON Format
```json
{
  "filename": "sample.pdf",
  "content_types": {
    "text_blocks": [
      {
        "id": "text_0",
        "content": "Introduction to Machine Learning",
        "type": "header",
        "confidence": 0.95,
        "word_count": 4
      }
    ],
    "tables": [
      {
        "headers": ["Algorithm", "Type", "Accuracy"],
        "rows": [["SVM", "Supervised", "0.92"]],
        "confidence": 0.88
      }
    ]
  },
  "statistics": {
    "total_text_blocks": 15,
    "total_images": 3,
    "total_tables": 2,
    "total_equations": 1
  }
}
```

### Markdown Format
```markdown
# Parsing Results: sample.pdf

## 📊 Statistics
- **Total Text Blocks:** 15
- **Total Images:** 3
- **Total Tables:** 2

## 📝 Text Content
### Text Block 1 (Header)
**Words:** 4 | **Confidence:** 0.95
```
Introduction to Machine Learning
```
```

## 🔧 Architecture Testing

### Parser Initialization
- Tests RAG-Anything configuration loading
- Validates multi-modal processor setup
- Confirms parsing engine selection

### Content Processing Pipeline
1. **File Upload** → Temporary storage and validation
2. **Parser Dispatch** → Route to appropriate content processors
3. **Multi-Modal Extraction** → Simultaneous text, image, table, equation processing
4. **Result Aggregation** → Combine outputs with confidence scoring
5. **Format Generation** → Create JSON and Markdown representations

### Confidence Scoring
Each extracted element includes confidence scores:
- **0.9-1.0**: High confidence, reliable extraction
- **0.7-0.9**: Good confidence, likely accurate
- **0.5-0.7**: Medium confidence, review recommended
- **0.0-0.5**: Low confidence, manual verification needed

## 🧪 Testing Scenarios

### Recommended Test Documents

1. **PDF with Mixed Content**: Academic papers with text, images, tables, equations
2. **Word Documents**: Reports with formatted text and embedded objects
3. **PowerPoint Presentations**: Slides with varied content layouts
4. **Excel Spreadsheets**: Data tables with headers and formulas
5. **Image Files**: Screenshots, diagrams, charts for OCR testing
6. **Text Files**: Markdown, plain text for baseline parsing

### Testing Checklist

- [ ] Parser initializes without errors
- [ ] All file types upload successfully
- [ ] Content extraction works for each type
- [ ] Confidence scores are reasonable
- [ ] JSON output is valid and complete
- [ ] Markdown formatting is correct
- [ ] Processing times are acceptable
- [ ] Error handling works properly

## 🐛 Troubleshooting

### Common Issues

**Parser Initialization Fails**
- Install RAG-Anything: `pip install raganything`
- Fallback to mock parser for demonstration

**File Upload Errors**
- Check file size (max 50MB)
- Verify supported file format
- Ensure file is not corrupted

**Parsing Takes Too Long**
- Large files may need several minutes
- Try smaller test files first
- Check system memory availability

**Missing Content Types**
- Verify processing options are enabled
- Some files may not contain all content types
- Check confidence scores for extraction quality

## 📈 Performance Notes

- **Processing Speed**: Varies by file size and complexity
- **Memory Usage**: ~500MB-2GB depending on document
- **File Size Limits**: 50MB maximum (configurable)
- **Concurrent Processing**: Single document at a time

## 🔮 Next Steps

After validating the parsing architecture:

1. **Integrate with Vector Store**: Add parsed content to vector database
2. **Implement RAG Pipeline**: Connect to LLM for question-answering
3. **Add Batch Processing**: Process multiple documents simultaneously
4. **Enhance Visualization**: Add content relationship graphs
5. **Performance Optimization**: Implement parallel processing

## 📝 License

MIT License - see LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Test parsing accuracy with your documents
3. Report issues or improvements
4. Submit pull requests with enhancements

---

**Built for RAG-Anything Architecture Testing**

*This demo focuses purely on parsing capabilities to validate the multi-modal content extraction pipeline before integrating with LLM components.*