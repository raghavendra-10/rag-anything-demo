# RAG-Anything Parser - Deployment Guide

## 🚀 Streamlit Cloud Deployment

### **Quick Deploy**

1. **Fork/Clone this repository**
2. **Push to your GitHub**
3. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select this repository
   - Main file: `app.py`
   - Click "Deploy"

### **Files Required for Cloud Deployment**

✅ **Already configured:**
- `packages.txt` - System dependencies (tesseract, poppler)
- `requirements.txt` - Python packages (cloud-optimized)
- `.streamlit/config.toml` - Streamlit configuration
- `app.py` - Main application

### **Deployment Status**

🟢 **Working Features:**
- PDF text extraction
- DOCX document parsing
- Excel spreadsheet parsing
- Text file processing
- Image metadata extraction
- JSON/Markdown output

🟡 **Limited Features (Cloud):**
- OCR text extraction (depends on tesseract availability)
- Advanced image processing (limited OpenCV)

## 🐳 Docker Deployment

### **Create Dockerfile**

```dockerfile
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    poppler-utils \
    libmagic1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### **Build and Run Docker**

```bash
# Build image
docker build -t rag-anything-parser .

# Run container
docker run -p 8501:8501 rag-anything-parser
```

## 🌐 Self-Hosted Server Deployment

### **Ubuntu/Debian Server**

```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y tesseract-ocr poppler-utils python3-pip

# Clone repository
git clone https://github.com/yourusername/rag-anything-demo.git
cd rag-anything-demo

# Install Python dependencies
pip3 install -r requirements.txt

# Run with systemd service
sudo tee /etc/systemd/system/rag-parser.service > /dev/null <<EOF
[Unit]
Description=RAG-Anything Parser
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/rag-anything-demo
ExecStart=/usr/local/bin/streamlit run app.py --server.port 8501 --server.address 0.0.0.0
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Enable and start service
sudo systemctl enable rag-parser
sudo systemctl start rag-parser
```

## ☁️ Cloud Platform Options

### **1. Streamlit Cloud** (Recommended)
- ✅ Free hosting
- ✅ Auto-deployment from GitHub
- ✅ Built-in SSL
- ⚠️ Resource limitations

### **2. Heroku**
```bash
# Create Procfile
echo "web: streamlit run app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile

# Add buildpacks
heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-apt
heroku buildpacks:add --index 2 heroku/python

# Deploy
git push heroku main
```

### **3. Railway**
- Connect GitHub repository
- Auto-detects Streamlit app
- One-click deployment

### **4. Google Cloud Run**
```bash
# Build and deploy
gcloud run deploy rag-parser \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## 🔧 Configuration for Production

### **Environment Variables**
```bash
# Optional: Set in deployment platform
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=8501
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

### **Performance Optimization**
- Use `opencv-python-headless` for cloud deployment
- Enable CPU-only PyTorch for faster startup
- Limit max upload size to prevent memory issues

### **Monitoring**
- Monitor memory usage (large PDF processing)
- Set up logging for parsing errors
- Track processing times

## 🚨 Troubleshooting

### **Common Issues**

1. **Tesseract not found**
   - Ensure `packages.txt` includes `tesseract-ocr`
   - Check system dependencies installation

2. **Memory limits**
   - Reduce max file size in config
   - Process files in chunks

3. **Import errors**
   - Verify all dependencies in `requirements.txt`
   - Check Python version compatibility

### **Debug Mode**
Add to `app.py` for debugging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📊 Deployment Checklist

- [ ] Repository pushed to GitHub
- [ ] `packages.txt` configured
- [ ] `requirements.txt` optimized for cloud
- [ ] `.streamlit/config.toml` added
- [ ] File upload limits set appropriately
- [ ] Error handling for missing dependencies
- [ ] Streamlit Cloud app deployed
- [ ] Testing with various file types
- [ ] Performance monitoring setup

## 🎯 Post-Deployment

1. **Test all file types** (PDF, DOCX, XLSX, images)
2. **Verify OCR functionality** 
3. **Check JSON/Markdown outputs**
4. **Monitor resource usage**
5. **Set up analytics** (optional)

Your RAG-Anything parser is now ready for production! 🚀