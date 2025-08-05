"""
Configuration management for RAG-Anything Parsing Demo
Focused on multi-modal content parsing without LLM integration
"""
import os
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
import streamlit as st

@dataclass
class ProcessingConfig:
    """Configuration for document processing options"""
    enable_image_processing: bool = True
    enable_table_processing: bool = True
    enable_equation_processing: bool = True
    parser_type: str = "auto"  # "mineru" or "auto"
    max_file_size_mb: int = 50
    chunk_size: int = 1000
    chunk_overlap: int = 200
    output_formats: List[str] = None  # ["json", "markdown"]
    
    def __post_init__(self):
        if self.output_formats is None:
            self.output_formats = ["json", "markdown"]

@dataclass
class UIConfig:
    """Configuration for UI elements"""
    page_title: str = "RAG-Anything Multi-Modal Parser Demo"
    page_icon: str = "🔍"
    layout: str = "wide"
    sidebar_width: int = 300
    max_display_items: int = 100

class AppConfig:
    """Main application configuration manager"""
    
    def __init__(self):
        self.processing = ProcessingConfig()
        self.ui = UIConfig()
        self.supported_file_types = {
            "pdf": ["pdf"],
            "document": ["docx", "doc"],
            "presentation": ["pptx", "ppt"],
            "spreadsheet": ["xlsx", "xls"],
            "image": ["png", "jpg", "jpeg", "gif", "bmp"],
            "text": ["txt", "md", "rtf"]
        }
        
    def get_supported_extensions(self) -> List[str]:
        """Get all supported file extensions"""
        extensions = []
        for file_types in self.supported_file_types.values():
            extensions.extend(file_types)
        return extensions
    
    def get_file_type(self, filename: str) -> Optional[str]:
        """Determine file type from filename"""
        if not filename or '.' not in filename:
            return None
            
        extension = filename.lower().split('.')[-1]
        for file_type, extensions in self.supported_file_types.items():
            if extension in extensions:
                return file_type
        return None
    
    def validate_file(self, file) -> tuple[bool, str]:
        """Validate uploaded file"""
        if file is None:
            return False, "No file uploaded"
        
        # Check file extension
        file_type = self.get_file_type(file.name)
        if not file_type:
            supported = ", ".join(self.get_supported_extensions())
            return False, f"Unsupported file type. Supported types: {supported}"
        
        # Check file size
        if hasattr(file, 'size') and file.size > self.processing.max_file_size_mb * 1024 * 1024:
            return False, f"File too large. Maximum size: {self.processing.max_file_size_mb}MB"
        
        return True, "File is valid"
    
    def update_processing_config(self, **kwargs) -> None:
        """Update processing configuration"""
        for key, value in kwargs.items():
            if hasattr(self.processing, key):
                setattr(self.processing, key, value)

# Global configuration instance
config = AppConfig()

# Streamlit page configuration
def setup_page_config():
    """Setup Streamlit page configuration"""
    st.set_page_config(
        page_title=config.ui.page_title,
        page_icon=config.ui.page_icon,
        layout=config.ui.layout,
        initial_sidebar_state="expanded"
    )

# CSS styling
def load_custom_css():
    """Load custom CSS for better UI"""
    st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: linear-gradient(90deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 0.5rem 0;
    }
    
    .content-section {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    .upload-section {
        border: 2px dashed #1f77b4;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        background: #f8f9ff;
    }
    
    .processing-badge {
        background: #28a745;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    
    .error-message {
        background: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #dc3545;
        margin: 1rem 0;
    }
    
    .success-message {
        background: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    
    .code-block {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 5px;
        padding: 1rem;
        font-family: monospace;
        white-space: pre-wrap;
        overflow-x: auto;
    }
    </style>
    """, unsafe_allow_html=True)