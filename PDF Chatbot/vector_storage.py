import os
import torch
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_vector_store(text_chunks):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"FAISS is running on: {device.upper()}")

    embeddings = HuggingFaceEmbeddings(model_name="hkunlp/instructor-xl", model_kwargs={"device": device})
    vector_db = FAISS.from_texts(text_chunks, embedding=embeddings)

    os.makedirs("faiss_index", exist_ok=True)
    vector_db.save_local("faiss_index")
    return vector_db
