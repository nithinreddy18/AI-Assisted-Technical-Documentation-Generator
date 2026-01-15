import streamlit as st
import requests
import json

# Page Configuration
st.set_page_config(page_title="AI Doc Generator", layout="wide")

st.title("🤖 AI-Assisted Documentation Generator")
st.markdown("Paste your Python code below, and the AI will generate professional documentation and a downloadable file.")

# --- 1. INPUT SECTION ---
with st.sidebar:
    st.header("Input Controls")
    generate_btn = st.button("Generate Documentation", type="primary")
    st.info("Ensure your Backend API is running on port 8000.")

source_code = st.text_area("Paste Python Code Here:", height=400, placeholder="def my_function():\n    pass")

# --- 2. LOGIC SECTION ---
if generate_btn and source_code:
    with st.spinner("Analyzing code structure and generating docs..."):
        try:
            # Call the FastAPI Backend
            response = requests.post(
                "http://127.0.0.1:8000/generate-docs",
                json={"source_code": source_code}
            )

            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])
                
                # --- 3. OUTPUT DISPLAY ---
                st.success(f"Successfully documented {len(results)} entities!")
                
                # Prepare Markdown content for the file
                markdown_file_content = "# AI Generated Documentation\n\n"
                
                for item in results:
                    entity_name = item['entity_name']
                    docstring = item['generated_docstring']
                    
                    # Display on screen
                    with st.expander(f"📝 {item['entity_type'].upper()}: {entity_name}", expanded=True):
                        st.markdown(f"**AI Explanation:**\n> {docstring}")
                        st.code(item['original_code'], language='python')
                    
                    # Add to markdown file content
                    markdown_file_content += f"## {entity_name} ({item['entity_type']})\n"
                    markdown_file_content += f"**Description:** {docstring}\n\n"
                    markdown_file_content += "```python\n" + item['original_code'] + "\n```\n\n"
                    markdown_file_content += "---\n\n"

                # --- 4. DOWNLOAD SECTION ---
                st.sidebar.markdown("---")
                st.sidebar.header("Export")
                st.sidebar.download_button(
                    label="📥 Download Documentation (.md)",
                    data=markdown_file_content,
                    file_name="documentation.md",
                    mime="text/markdown"
                )

            else:
                st.error(f"Error {response.status_code}: {response.text}")

        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to the Backend API. Is it running?")
else:
    if generate_btn:
        st.warning("Please paste some code first.")
