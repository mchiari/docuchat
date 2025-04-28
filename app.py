import streamlit as st
import os
from utils import pdf_processor, embeddings, chatbot, docling_processor
from dotenv import load_dotenv
from streamlit_chat import message

load_dotenv()

def main():

    st.set_page_config(page_title="Docuchat - Chat with your files", page_icon=":books:", layout="wide")
    st.title("Docuchat - Chat with your files")
    st.header("Chat with your files using Langchain and OpenAI")
    st.write("Made for AI First Contest")


    if("conversation" not in st.session_state):
        st.session_state.conversation = None

    user_question = st.text_input("Ask a question about your files:")
    
    if user_question:
        response = st.session_state.conversation(user_question)['chat_history']
        # st.info(response)
        for i, text in enumerate(response):
            if i % 2 == 0:
                message(text.content, is_user=True, key=f"user_{i}")
            else:
                message(text.content, is_user=False, key=f"bot_{i}")
    


    with st.sidebar:
        st.subheader("Seus arquivos")
        uploaded_docs = st.file_uploader("Upload files", accept_multiple_files=True)
        if uploaded_docs:
            st.success("Files uploaded successfully!")


        if st.button("Process Files"):
            if uploaded_docs:

                text_from_docs = docling_processor.convert_document_to_md(uploaded_docs)
                # print(text_from_docs)

                st.success("Files processed successfully!")
                # print(text_from_docs)
                # st.info("Processing files...")
                # text_from_docs = pdf_processor.extract_text(uploaded_docs)
                # st.success("Files processed successfully!")

                chunks = pdf_processor.create_text_chunks(text_from_docs)
                st.success("Text chunks created successfully!")

                vector_store = embeddings.create_vector_store(chunks)
                st.success("Vector store created successfully!")

                st.session_state.conversation = chatbot.create_conversation_chain(vector_store)
                st.success("Conversation chain created successfully!")

                # print(text_from_docs)
            else:
                st.error("Please upload at least one PDF file before processing.", icon="⚠️")

if __name__ == "__main__":

    main()