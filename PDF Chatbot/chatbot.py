from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def load_faiss_database():
    embeddings = HuggingFaceEmbeddings(model_name="hkunlp/instructor-xl")
    vector_db = FAISS.load_local("faiss_index", embeddings=embeddings, allow_dangerous_deserialization=True)
    return vector_db.as_retriever()

def setup_chatbot():
    retriever = load_faiss_database()
    llm = HuggingFaceEndpoint(
        endpoint_url="https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct",
        huggingfacehub_api_token='HUGGINGFACEHUB_API_TOKEN',
        temperature=0.3,
        model_kwargs={"max_length": 512}
    )

    memory = ConversationBufferWindowMemory(k=5, memory_key="chat_history", return_messages=True)

    chatbot = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory
    )

    return chatbot

def ask_chatbot(query):
    chatbot = setup_chatbot()
    response = chatbot.invoke({"question": query})
    return response

if __name__ == '__main__':
    query = input("Ask a question: ")
    response = ask_chatbot(query)
    print("\nChatbot Response\n", response)