from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

def create_conversation_chain(vector_store):
    llm = ChatOpenAI(temperature=0)

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    retriever = vector_store.as_retriever()

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
    )

    return conversation_chain