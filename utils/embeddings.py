from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os

def create_vector_store(text_chunks):
    """
    Create a vector store from the text chunks using OpenAI embeddings.
    """

    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key is None:
        raise ValueError("OPENAI_API_KEY environment variable not set.")

    embeddings = OpenAIEmbeddings(api_key=api_key)
    
    vector_store = FAISS.from_texts(text_chunks, embeddings)
    
    return vector_store