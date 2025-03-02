import os
from PyPDF2 import PdfReader

UPLOAD_FOLDER = "uploads"

def extract_text_from_pdfs(pdf_files):
    text = ""
    for pdf in pdf_files:
        pdf_path = os.path.join(UPLOAD_FOLDER, pdf)  
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    return text

if __name__ == "__main__":
    uploaded_pdfs = os.listdir(UPLOAD_FOLDER)
    extracted_text = extract_text_from_pdfs(uploaded_pdfs)
    print(extracted_text)
