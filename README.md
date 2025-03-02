# PDF Reader Chatbot

![PDF Reader Chatbot](https://github.com/aryannnb1/PDF-Reader-Chatbot/blob/main/Screenshot%20(1014).png)

## Description
A full-stack project for a PDF Reader Chatbot designed to assist users in reading and interacting with PDF files. Users can upload PDFs, ask questions about the content, and receive responses from the chatbot.

## Features
- Upload and interact with PDF files
- Receive accurate responses from the chatbot
- Multi-language support (Python, CSS, JavaScript, HTML)

## Technologies Used
- **Python**: Backend logic and PDF processing
- **CSS**: Styling for the user interface
- **JavaScript**: Frontend interactivity
- **HTML**: Structure of the web pages

## Libraries Used
- **Flask**: Web framework
- **Werkzeug**: WSGI web application library
- **PyPDF2**: PDF file manipulation
- **langchain**: Language model applications
- **langchain_huggingface**: Hugging Face integration
- **langchain_community**: Community-driven extensions
- **python-dotenv**: Environment variables

## GPU Utilization
GPU acceleration is used for efficient processing and inference with large PDF files and complex language models.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/aryannnb1/PDF-Reader-Chatbot.git
   ```
2. Navigate to the project directory:
   ```sh
   cd PDF-Reader-Chatbot
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```sh
   python app.py
   ```
2. Open `http://localhost:5000` in your browser
3. Upload a PDF and start interacting with the chatbot.

## File Structure
```
PDF-Reader-Chatbot/
├── PDF Chatbot/
│   ├── __init__.py
│   ├── app.py
│   ├── chatbot.py
│   ├── document_pipeline.py
│   ├── requirements.txt
│   ├── static/
│   ├── templates/
│   ├── vector_storage.py
├── .env
├── .gitignore
├── LICENSE
├── README.md
```

## Acknowledgements
- [Flask](https://flask.palletsprojects.com/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [Hugging Face](https://huggingface.co/)
