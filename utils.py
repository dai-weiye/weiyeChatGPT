from langchain.chains import ConversationChain
from langchain_community.chat_models  import ChatTongyi

import os

from langchain.memory import ConversationBufferMemory

def get_chat_response(prompt, memory, DASHSCOPE_API_KE):

    model = ChatTongyi(model="qwen-72b-chat", DASHSCOPE_API_KE=DASHSCOPE_API_KE)
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]

