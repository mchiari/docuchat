from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter


def extract_text(pdf):

    text = ''

    for file in pdf:
        pdf = PdfReader(file)

        for page in pdf.pages:
            text += page.extract_text()

    return text

def create_text_chunks(text):

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1500,
        chunk_overlap=200,
        length_function=len,
    )

    text_chunks = text_splitter.split_text(text)
    return text_chunks