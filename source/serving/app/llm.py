from langchain_community.chat_models import ChatOllama

# Langchain이 지원하는 다른 채팅 모델을 사용합니다. 여기서는 Ollama를 사용합니다.
llm = ChatOllama(model="enjoy-bot-8b:latest", temperature=0) 
