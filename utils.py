from langchain.chains import ConversationChain
from langchain_community.chat_models  import ChatTongyi

import os

from langchain.memory import ConversationBufferMemory

def get_chat_response(prompt, memory, DASHSCOPE_API_KE):

    model = ChatTongyi(model="qwen-72b-chat", DASHSCOPE_API_KE=DASHSCOPE_API_KE)
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]


 #memory = ConversationBufferMemory(return_messages=True)
 #print(get_chat_response("牛顿提出过哪些知名的定律？", memory, os.getenv("DASHSCOPE_API_KE")))
 #print(get_chat_response("我上一个问题是什么？", memory, os.getenv("DASHSCOPE_API_KE")))
