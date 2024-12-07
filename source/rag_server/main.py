import os
import streamlit as st
from app.chat_app import ChatApp

@st.cache_resource
def load_app():
    current_dir = os.getcwd()

    project_name = "openllm-bizguidebot"
    if current_dir.startswith("/home"):
        document_dir = os.path.abspath(os.path.join(current_dir, "../../document"))
    else:
        document_dir = f"/mount/src/{project_name}/document"
    
    print("여기도 다시 init?")
    return ChatApp({
        "llm_url": "https://complete-mastiff-special.ngrok-free.app/llm/",
        "document_dir": document_dir,
        "show_prompt" : True,
    })

def main():
    app = load_app()
    app.run()

if __name__ == "__main__":
    main()
