from pdf_processing import extract_text_from_pdfs
from text_splitter import split_text_into_chunks
from vector_storage import create_vector_store

def process_pdfs(pdf_files):
    raw_text = extract_text_from_pdfs(pdf_files)
    text_chunks = split_text_into_chunks(raw_text)
    return text_chunks