from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def _extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf = PdfReader(file)
        text = " ".join(page.extract_text() for page in pdf.pages)
    return text

def chunk_pdf_file(file_path: str) -> list[str]:
    text = _extract_text_from_pdf(file_path)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 300,
        chunk_overlap  = 30,
        length_function = len,
        separators = ['\n']
    )

    split_texts = splitter.create_documents([text])
    return [x.page_content for x in split_texts]
