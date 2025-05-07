from docling.document_converter import DocumentConverter



def main():

    url = "https://esaj.tjsp.jus.br/cpopg/show.do?processo.codigo=2S001XX7O0000&processo.foro=100&processo.numero=1181992-28.2024.8.26.0100&gateway=true"
    convert_html_to_md(url)


def convert_html_to_md(url) -> str:
    converter = DocumentConverter()
    result = converter.convert(url)
    print(result)

    document = result.document
    markdown_output = document.export_to_markdown()
    return markdown_output


if __name__ == "__main__":

    main()