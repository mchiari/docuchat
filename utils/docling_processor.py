from langchain.text_splitter import CharacterTextSplitter
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import DocumentStream
from utils import embeddings
import io


def execute(docs):

    if(docs):

        # url = "https://esaj.tjsp.jus.br/cpopg/show.do?processo.codigo=2S001XX7O0000"
        # text = convert_html_to_md(url)
        text = convert_document_to_md(docs)

        # text = convert_html_to_md()
        chunks = create_text_chunks(text)

        # for file in docs:
            # file_name = file.name.split(".")[0]
            # save_text_chunks(chunks, file_name)

        store = embeddings.create_vector_store(chunks)

        return store



def convert_document_to_md(files: str) -> str:
    text = ''
    
    for file in files:

        buffer = io.BytesIO(file.read())
        source = DocumentStream(name='test', stream=buffer)
        converter = DocumentConverter()
        result = converter.convert(source)
        # print(result)

        text = result.document.export_to_text() + '\n\n' + text

    return text


def create_text_chunks(text) -> list:
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=6000,
        chunk_overlap=200,
        length_function=len,
    )

    text_chunks = text_splitter.split_text(text)

    return text_chunks


def save_text_chunks(text_chunks, file_name):
    with open(f"./data/{file_name}.txt", "w") as file:
        for chunk in text_chunks:
            file.write(chunk + "\n\n")
        file.close()






def convert_html_to_md(url) -> str:
    converter = DocumentConverter()
    result = converter.convert(url)

    document = result.document
    markdown_output = document.export_to_markdown()
    print(markdown_output)
    return markdown_output
