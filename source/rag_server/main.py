import os
from app.chat_app import ChatApp

def load_app():
    current_dir = os.getcwd()

    project_name = "openllm-bizguidebot"
    if current_dir.startswith("/home"):
        document_dir = os.path.abspath(os.path.join(current_dir, "../../document"))
    else:
        document_dir = f"/mount/src/{project_name}/document"
    
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
