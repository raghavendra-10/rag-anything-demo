"""
RAG-Anything Multi-Modal Content Parser Demo
Focused on demonstrating parsing capabilities without LLM integration
"""
import streamlit as st
import pandas as pd
from typing import Dict, Any

# Import our custom modules
from config import config, setup_page_config, load_custom_css
from utils import ContentParser, OutputFormatter, FileUtils, truncate_text, create_metrics_display

# Page configuration
setup_page_config()
load_custom_css()

class RAGParsingDemo:
    """Main application class for the RAG-Anything parsing demo"""
    
    def __init__(self):
        self.parser = ContentParser(config)
        self.formatter = OutputFormatter()
        self.file_utils = FileUtils()
        
        # Initialize session state
        if "parsing_results" not in st.session_state:
            st.session_state.parsing_results = {}
        if "current_file" not in st.session_state:
            st.session_state.current_file = None
        if "parser_initialized" not in st.session_state:
            st.session_state.parser_initialized = False
        
        # Auto-initialize parser on startup
        self._auto_initialize_parser()
    
    def _auto_initialize_parser(self):
        """Auto-initialize parser on application startup"""
        if not st.session_state.parser_initialized:
            try:
                # Force initialization
                success = self.parser.initialize_parser()
                if success and self.parser.rag_instance is not None:
                    st.session_state.parser_initialized = True
                    # Store parser status for debugging
                    st.session_state.parser_status = "Auto-initialized successfully"
                else:
                    st.session_state.parser_status = "Auto-initialization failed"
            except Exception as e:
                st.session_state.parser_status = f"Auto-initialization error: {str(e)}"
                # No fallback - real parsing only
    
    def render_header(self):
        """Render the application header"""
        st.markdown('<h1 class="main-header">🔍 RAG-Anything Multi-Modal Parser</h1>', 
                   unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem; color: #666;">
        Demonstrate RAG-Anything's multi-modal content parsing architecture.<br>
        Upload documents to see how different content types are extracted and structured <strong>without LLM integration</strong>.
        </div>
        """, unsafe_allow_html=True)
        
        # Show parser status
        if not st.session_state.parser_initialized:
            st.warning("⚠️ Parser initialization failed. Click 'Initialize Parser' in the sidebar to retry.")
            # Debug information
            if "parser_status" in st.session_state:
                st.caption(f"Debug: {st.session_state.parser_status}")
        else:
            st.success("✅ Parser ready for document processing")
            # Show parser information
            if hasattr(self.parser, 'rag_instance') and self.parser.rag_instance:
                parser_type = type(self.parser.rag_instance).__name__
                st.success("🚀 Using Real RAG Parser")
                st.caption("Multi-modal document parsing with LightRAG")
                st.caption(f"Parser: {parser_type}")
            
            # Show available capabilities
            if hasattr(self.parser, 'rag_instance') and hasattr(self.parser.rag_instance, 'ocr_available'):
                capabilities = []
                if self.parser.rag_instance.ocr_available:
                    capabilities.append("OCR")
                if hasattr(self.parser.rag_instance, 'docx_available') and self.parser.rag_instance.docx_available:
                    capabilities.append("DOCX")
                if hasattr(self.parser.rag_instance, 'excel_available') and self.parser.rag_instance.excel_available:
                    capabilities.append("Excel")
                
                if capabilities:
                    st.caption(f"Capabilities: {', '.join(capabilities)}")
            
            # Debug information
            if "parser_status" in st.session_state:
                st.caption(f"Status: {st.session_state.parser_status}")
    
    def render_sidebar(self):
        """Render the sidebar with configuration options"""
        with st.sidebar:
            st.header("⚙️ Parser Configuration")
            
            # Parser Status
            st.subheader("🚀 Parser Status")
            
            if st.session_state.parser_initialized:
                st.success("✅ Parser Ready")
                st.caption("Auto-initialized on startup")
                
                # Show parser type in sidebar
                if hasattr(self.parser, 'rag_instance') and self.parser.rag_instance:
                    parser_type = type(self.parser.rag_instance).__name__
                    st.info("🚀 Real RAG Mode")
                    st.caption("Multi-modal parsing active")
            else:
                st.warning("⚠️ Parser not initialized")
                if st.button("🔧 Initialize RAG-Anything Parser", type="primary"):
                    with st.spinner("Initializing parser..."):
                        success = self.parser.initialize_parser()
                        if success:
                            st.session_state.parser_initialized = True
                            st.success("✅ Parser initialized!")
                            st.rerun()
                        else:
                            st.error("❌ Failed to initialize parser")
            
            st.divider()
            
            # Processing Configuration
            st.subheader("🛠️ Processing Options")
            
            enable_images = st.checkbox(
                "Enable Image Processing",
                value=config.processing.enable_image_processing,
                help="Extract and analyze images with captions",
                disabled=not st.session_state.parser_initialized
            )
            
            enable_tables = st.checkbox(
                "Enable Table Processing",
                value=config.processing.enable_table_processing,
                help="Extract and structure table content",
                disabled=not st.session_state.parser_initialized
            )
            
            enable_equations = st.checkbox(
                "Enable Equation Processing",
                value=config.processing.enable_equation_processing,
                help="Detect and parse mathematical equations",
                disabled=not st.session_state.parser_initialized
            )
            
            parser_type = st.selectbox(
                "Parser Type",
                options=["auto", "mineru"],
                index=0 if config.processing.parser_type == "auto" else 1,
                help="Choose the parsing engine",
                disabled=not st.session_state.parser_initialized
            )
            
            # Update configuration
            config.update_processing_config(
                enable_image_processing=enable_images,
                enable_table_processing=enable_tables,
                enable_equation_processing=enable_equations,
                parser_type=parser_type
            )
            
            st.divider()
            
            # Output Format Selection
            st.subheader("📤 Output Formats")
            output_formats = st.multiselect(
                "Select output formats:",
                options=["json", "markdown"],
                default=["json", "markdown"],
                help="Choose how to display parsing results"
            )
            config.processing.output_formats = output_formats
            
            st.divider()
            
            # File Information
            if st.session_state.current_file:
                st.subheader("📄 Current File")
                file_info = st.session_state.current_file
                st.write(f"**Name:** {file_info['name']}")
                st.write(f"**Type:** {file_info['type']}")
                st.write(f"**Size:** {file_info['size']:.1f} KB")
    
    def render_upload_section(self):
        """Render the file upload section"""
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("📤 Upload Document for Parsing")
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Choose a file to parse",
            type=config.get_supported_extensions(),
            help=f"Supported formats: {', '.join(config.get_supported_extensions())}"
        )
        
        if uploaded_file is not None:
            # Validate file
            is_valid, message = config.validate_file(uploaded_file)
            
            if is_valid:
                # Store file information
                st.session_state.current_file = {
                    "name": uploaded_file.name,
                    "type": config.get_file_type(uploaded_file.name),
                    "size": uploaded_file.size / 1024  # Convert to KB
                }
                
                st.success(f"✅ {message}")
                
                # Parse button
                col1, col2 = st.columns([3, 1])
                with col1:
                    parse_button = st.button(
                        "🚀 Parse Document", 
                        type="primary", 
                        disabled=not st.session_state.parser_initialized,
                        use_container_width=True
                    )
                
                with col2:
                    if st.button("🗑️ Clear", help="Clear current file"):
                        st.session_state.current_file = None
                        st.rerun()
                
                if parse_button:
                    if not st.session_state.parser_initialized:
                        st.error("❌ Please initialize the parser first in the sidebar")
                    else:
                        self.parse_uploaded_file(uploaded_file)
            else:
                st.error(f"❌ {message}")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    def parse_uploaded_file(self, uploaded_file):
        """Parse the uploaded file with RAG-Anything"""
        # Save file temporarily
        temp_file_path = self.file_utils.save_uploaded_file(uploaded_file)
        
        if not temp_file_path:
            st.error("❌ Failed to save uploaded file")
            return
        
        try:
            # Parse document
            results = self.parser.parse_document(temp_file_path, uploaded_file.name)
            
            if "error" not in results:
                # Store results
                st.session_state.parsing_results[uploaded_file.name] = results
                st.success("✅ Document parsed successfully!")
                
                # Auto-scroll to results
                st.markdown('<div id="results"></div>', unsafe_allow_html=True)
            else:
                st.error(f"❌ Parsing failed: {results.get('error', 'Unknown error')}")
            
        except Exception as e:
            st.error(f"❌ Error parsing document: {str(e)}")
        
        finally:
            # Cleanup temporary file
            self.file_utils.cleanup_temp_file(temp_file_path)
    
    def render_results_section(self):
        """Render the parsing results section"""
        if not st.session_state.parsing_results:
            st.info("📋 No documents parsed yet. Upload a file to see parsing results.")
            return
        
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("📊 Parsing Results")
        
        # File selector
        selected_file = st.selectbox(
            "Select parsed file:",
            options=list(st.session_state.parsing_results.keys()),
            key="file_selector"
        )
        
        if selected_file:
            results = st.session_state.parsing_results[selected_file]
            
            # Display overview metrics
            self.render_overview_metrics(results)
            
            # Display parsing results in tabs
            self.render_parsing_results_tabs(results)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    def render_overview_metrics(self, results: Dict[str, Any]):
        """Render overview metrics cards"""
        st.subheader("📈 Parsing Overview")
        
        statistics = results.get("statistics", {})
        create_metrics_display(statistics)
        
        # Additional metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="Total Words",
                value=statistics.get("total_words", 0),
                help="Total word count across all text content"
            )
        
        with col2:
            st.metric(
                label="Total Characters",
                value=statistics.get("total_characters", 0),
                help="Total character count"
            )
        
        with col3:
            processing_time = results.get("processing_time", "Unknown")
            if isinstance(processing_time, str) and 'T' in processing_time:
                display_time = processing_time.split('T')[1].split('.')[0]
            else:
                display_time = str(processing_time)
            st.metric(
                label="Processing Time",
                value=display_time,
                help="When the document was processed"
            )
    
    def render_parsing_results_tabs(self, results: Dict[str, Any]):
        """Render tabbed view of parsing results"""
        st.subheader("📑 Detailed Parsing Results")
        
        # Create tabs based on available output formats
        output_formats = config.processing.output_formats
        tab_names = []
        tabs = []
        
        # Always include content tabs
        tab_names.extend(["📝 Text", "🖼️ Images", "📊 Tables", "🧮 Equations"])
        
        # Add output format tabs
        if "json" in output_formats:
            tab_names.append("📄 JSON")
        if "markdown" in output_formats:
            tab_names.append("📋 Markdown")
        
        # Create tabs
        tabs = st.tabs(tab_names)
        
        content_types = results.get("content_types", {})
        tab_idx = 0
        
        # Text content tab
        with tabs[tab_idx]:
            self.render_text_content(content_types.get("text_blocks", []))
        tab_idx += 1
        
        # Images tab
        with tabs[tab_idx]:
            self.render_image_content(content_types.get("images", []))
        tab_idx += 1
        
        # Tables tab
        with tabs[tab_idx]:
            self.render_table_content(content_types.get("tables", []))
        tab_idx += 1
        
        # Equations tab
        with tabs[tab_idx]:
            self.render_equation_content(content_types.get("equations", []))
        tab_idx += 1
        
        # JSON output tab
        if "json" in output_formats:
            with tabs[tab_idx]:
                self.render_json_output(results)
            tab_idx += 1
        
        # Markdown output tab
        if "markdown" in output_formats:
            with tabs[tab_idx]:
                self.render_markdown_output(results)
    
    def render_text_content(self, text_blocks: list):
        """Render text content analysis"""
        if not text_blocks:
            st.info("No text blocks found in the document.")
            return
        
        st.write(f"Found **{len(text_blocks)}** text blocks:")
        
        for i, block in enumerate(text_blocks):
            block_type = block.get('type', 'unknown').title()
            word_count = block.get('word_count', 0)
            confidence = block.get('confidence', 1.0)
            
            with st.expander(f"Text Block {i+1}: {block_type} ({word_count} words) - Confidence: {confidence:.2f}"):
                st.write("**Content:**")
                st.code(block.get("content", ""), language="text")
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Type", block.get("type", "unknown"))
                with col2:
                    st.metric("Words", word_count)
                with col3:
                    st.metric("Length", block.get("length", 0))
                with col4:
                    st.metric("Line #", block.get("line_number", 0))
    
    def render_image_content(self, images: list):
        """Render image content analysis"""
        if not images:
            st.info("No images found in the document.")
            return
        
        st.write(f"Found **{len(images)}** images:")
        
        for i, img in enumerate(images):
            caption = img.get('caption', 'Untitled')
            confidence = img.get('confidence', 1.0)
            
            with st.expander(f"Image {i+1}: {caption} - Confidence: {confidence:.2f}"):
                st.write("**Caption:**", img.get("caption", "No caption"))
                st.write("**Description:**", img.get("description", "No description"))
                st.write("**Alt Text:**", img.get("alt_text", "No alt text"))
                
                extracted_text = img.get("extracted_text", "")
                if extracted_text:
                    st.write("**Extracted Text:**", extracted_text)
                
                metadata = img.get("metadata", {})
                if metadata:
                    st.write("**Metadata:**")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Width", metadata.get("width", "Unknown"))
                    with col2:
                        st.metric("Height", metadata.get("height", "Unknown"))
                    with col3:
                        st.metric("Format", metadata.get("format", "Unknown"))
    
    def render_table_content(self, tables: list):
        """Render table content analysis"""
        if not tables:
            st.info("No tables found in the document.")
            return
        
        st.write(f"Found **{len(tables)}** tables:")
        
        for i, table in enumerate(tables):
            caption = table.get('caption', 'Untitled')
            confidence = table.get('confidence', 1.0)
            row_count = table.get('row_count', 0)
            col_count = table.get('col_count', 0)
            
            with st.expander(f"Table {i+1}: {caption} ({row_count}×{col_count}) - Confidence: {confidence:.2f}"):
                st.write("**Caption:**", caption)
                
                # Display table data
                headers = table.get("headers", [])
                rows = table.get("rows", [])
                
                if headers and rows:
                    try:
                        df = pd.DataFrame(rows, columns=headers)
                        st.dataframe(df, use_container_width=True)
                    except Exception as e:
                        st.error(f"Error displaying table: {str(e)}")
                        st.write("**Headers:**", headers)
                        st.write("**Rows:**", rows)
                else:
                    st.write("Table structure not available")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Rows", row_count)
                with col2:
                    st.metric("Columns", col_count)
                with col3:
                    data_types = table.get("data_types", [])
                    st.metric("Data Types", len(data_types) if data_types else 0)
    
    def render_equation_content(self, equations: list):
        """Render equation content analysis"""
        if not equations:
            st.info("No equations found in the document.")
            return
        
        st.write(f"Found **{len(equations)}** equations:")
        
        for i, eq in enumerate(equations):
            description = eq.get('description', 'Mathematical expression')
            confidence = eq.get('confidence', 1.0)
            
            with st.expander(f"Equation {i+1}: {description} - Confidence: {confidence:.2f}"):
                st.write("**Description:**", description)
                st.write("**Type:**", eq.get("type", "unknown"))
                
                # Display LaTeX
                latex = eq.get("latex", "")
                if latex:
                    st.write("**LaTeX:**")
                    st.code(latex, language="latex")
                    
                    # Try to render the equation
                    try:
                        st.latex(latex)
                    except Exception as e:
                        st.write(f"Unable to render equation: {str(e)}")
                
                # Display variables and context
                variables = eq.get("variables", [])
                if variables:
                    st.write("**Variables:**", ", ".join(variables))
                
                context = eq.get("context", "")
                if context:
                    st.write("**Context:**", context)
    
    def render_json_output(self, results: Dict[str, Any]):
        """Render JSON formatted output"""
        st.write("**📄 JSON Output**")
        st.write("Complete parsing results in JSON format:")
        
        # Display formatted JSON
        json_output = self.formatter.to_json(results)
        st.code(json_output, language="json")
        
        # Download button
        st.download_button(
            label="📥 Download JSON",
            data=json_output,
            file_name=f"{results.get('filename', 'parsing_results')}.json",
            mime="application/json"
        )
    
    def render_markdown_output(self, results: Dict[str, Any]):
        """Render Markdown formatted output"""
        st.write("**📋 Markdown Output**")
        st.write("Parsing results formatted as Markdown:")
        
        # Generate and display markdown
        markdown_output = self.formatter.to_markdown(results)
        
        # Show markdown in two ways: rendered and raw
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Rendered View:**")
            st.markdown(markdown_output)
        
        with col2:
            st.write("**Raw Markdown:**")
            st.code(markdown_output, language="markdown")
        
        # Download button
        st.download_button(
            label="📥 Download Markdown",
            data=markdown_output,
            file_name=f"{results.get('filename', 'parsing_results')}.md",
            mime="text/markdown"
        )
    
    def run(self):
        """Main application runner"""
        # Render main components
        self.render_header()
        self.render_sidebar()
        
        # Main content area
        self.render_upload_section()
        
        st.divider()
        
        self.render_results_section()
        
        # Footer
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; color: #666; margin-top: 2rem;">
        <p>🚀 <strong>RAG-Anything Parsing Demo</strong> | Multi-Modal Content Parsing Architecture</p>
        <p>Built with Streamlit • Powered by RAG-Anything Parser (No LLM Integration)</p>
        <p><em>Focus: Testing multi-modal parsing capabilities and architecture</em></p>
        </div>
        """, unsafe_allow_html=True)

# Main execution
def main():
    """Main function to run the Streamlit app"""
    app = RAGParsingDemo()
    app.run()

if __name__ == "__main__":
    main()