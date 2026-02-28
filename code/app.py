import streamlit as st
import pandas as pd
from generator_logic import DataGeneratorLogic
import json

# Page Configuration
st.set_page_config(
    page_title="Synthetic Data Generator (AI-Powered)",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e1e2f 0%, #2d2d44 100%);
        color: #e0e0e0;
    }
    .stTextInput > div > div > input {
        background-color: #3d3d5c;
        color: white;
        border: 1px solid #5c5c8a;
    }
    .stButton > button {
        background-color: #6200ea;
        color: white;
        border-radius: 8px;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #7c4dff;
        border: 1px solid white;
    }
    .sidebar .sidebar-content {
        background-color: #161625;
    }
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        color: #bb86fc;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 AI-Driven Synthetic Data Generator")
st.markdown("Transform business requirements into realistic, referential datasets instantly.")

# Sidebar for API Configuration
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password", help="Get your key from Google AI Studio")
    st.info("Your API key is only used for the current session and is not stored.")
    
    st.divider()
    st.markdown("### How it works")
    st.markdown("1. Describe your business use case.\n2. AI infers the schema & relationships.\n3. AI generates a `faker` script.\n4. Run the script to get your CSVs.")

# Main Interface
if not api_key:
    st.warning("Please enter your Gemini API Key in the sidebar to begin.")
else:
    logic = DataGeneratorLogic(api_key)
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "schema" not in st.session_state:
        st.session_state.schema = None
    
    if "script" not in st.session_state:
        st.session_state.script = None

    # Chat history display
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Describe your business use case (e.g., 'E-commerce system with users, products, and orders')"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Designing Schema..."):
                schema = logic.infer_schema(prompt)
                if schema:
                    st.session_state.schema = schema
                    st.markdown("### ✅ Schema Inferred")
                    
                    # Display Schema Summary
                    for table in schema['tables']:
                        with st.expander(f"Table: {table['name']}"):
                            st.write(table['description'])
                            cols_df = pd.DataFrame(table['columns'])
                            st.table(cols_df[['name', 'type', 'is_pk', 'is_fk', 'references']])
                    
                    with st.spinner("Generating Faker Script..."):
                        script = logic.generate_faker_script(schema)
                        st.session_state.script = script
                        st.markdown("### 📜 Python Generation Script")
                        st.code(script, language='python')
                        
                        st.download_button(
                            label="Download Generator Script",
                            data=script,
                            file_name="generate_data.py",
                            mime="text/x-python"
                        )
                else:
                    st.error("Failed to infer schema. Please try a different prompt.")

# Footer
st.markdown("---")
st.markdown("Built By Jayan Gupta")
