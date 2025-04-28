from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import DocumentStream

import io

def convert_document_to_md(files: str) -> str:

    text = ''

    for file in files:

        buffer = io.BytesIO(file.read())
        source = DocumentStream(name='test', stream=buffer)
        converter = DocumentConverter()
        result = converter.convert(source)

        text = result.document.export_to_text() + '\n\n' + text

    return text