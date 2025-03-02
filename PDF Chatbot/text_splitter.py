from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text_into_chunks(text):
    splitter = RecursiveCharacterTextSplitter(
        separators=['\n'],
        chunk_size=800,
        chunk_overlap=100,
        length_function=len
    )
    return splitter.split_text(text)

if __name__ == "__main__":
    sample_text = "This is a test sentence. " * 100
    chunks = split_text_into_chunks(sample_text)

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:\n{chunk}\n")
