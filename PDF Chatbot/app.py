import os
import shutil
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from document_pipeline import process_pdfs
from vector_storage import create_vector_store
from chatbot import ask_chatbot

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
FAISS_FOLDER = "faiss_index"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(FAISS_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {"pdf"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_files():
    if not request.files:
        return jsonify({"error": "No files uploaded"}), 400

    files = request.files.getlist("files[]")
    saved_files = []


    if os.path.exists(UPLOAD_FOLDER):
        shutil.rmtree(UPLOAD_FOLDER)
        os.makedirs(UPLOAD_FOLDER)  
        print("Uploads folder cleared.")

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)
            saved_files.append(filename)
            print(f"Saved: {file_path}")

    if not saved_files:
        return jsonify({"error": "No valid PDF files uploaded"}), 400


    if os.path.exists(FAISS_FOLDER):
        shutil.rmtree(FAISS_FOLDER)
        os.makedirs(FAISS_FOLDER)  
        print("🗑️ FAISS database cleared.")

    print("Processing PDFs and updating FAISS database...")
    text_chunks = process_pdfs(saved_files)
    create_vector_store(text_chunks)
    print("FAISS vector store updated!")

    return jsonify({"message": "Files uploaded and processed successfully", "files": saved_files}), 200

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_query = data.get("message", "")

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    print(f"User asked: {user_query}")

    chatbot_response = ask_chatbot(user_query)

    print(f"Chatbot response: {chatbot_response}")

    return jsonify({"response": chatbot_response}), 200

if __name__ == "__main__":
    app.run(debug=True)
