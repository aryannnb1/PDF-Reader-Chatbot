# PDF Reader Chatbot

![PDF Reader Chatbot](path/to/your/image.png)

## Description
This is a full-stack project for a PDF Reader Chatbot. The chatbot is designed to assist users in reading and interacting with PDF files. Users can upload PDFs, ask questions about the content, and receive responses from the chatbot.

## Features
- Upload PDF files
- Interact with the chatbot to ask questions about the PDF content
- Receive accurate and relevant responses based on the PDF content
- Multi-language support (Python, CSS, JavaScript, HTML)

## Technologies Used
- **Python**: Backend logic and PDF processing (50%)
- **CSS**: Styling for the user interface (19.9%)
- **JavaScript**: Frontend interactivity (19.6%)
- **HTML**: Structure of the web pages (10.5%)

## Libraries Used
- **Flask**: A micro web framework used for creating the web application.
- **Werkzeug**: A comprehensive WSGI web application library used by Flask.
- **PyPDF2**: A library used for reading and manipulating PDF files.
- **langchain**: A library for building language model applications.
- **langchain_huggingface**: A Hugging Face integration for langchain.
- **langchain_community**: Community-driven extensions for langchain.
- **python-dotenv**: A library to read key-value pairs from a `.env` file and set them as environment variables.

## GPU Utilization
The project leverages GPU for efficient processing and inference when working with large PDF files and complex language models. The GPU acceleration is provided by the `langchain` library which integrates with Hugging Face models optimized for GPU.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/aryannnb1/PDF-Reader-Chatbot.git
   ```
2. Navigate to the project directory:
   ```sh
   cd PDF-Reader-Chatbot
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```sh
   python app.py
   ```
2. Open your web browser and go to `http://localhost:5000`
3. Upload a PDF file and start interacting with the chatbot.

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
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── scripts.js
│   ├── templates/
│   │   ├── index.html
│   ├── vector_storage.py
├── .env
├── .gitignore
├── LICENSE
├── README.md
```

### Description of Key Files and Directories
- `PDF Chatbot/`: Contains the main application code and related files.
  - `__init__.py`: Initializes the Python package.
  - `app.py`: The main application file that sets up the Flask app, handles file uploads, and processes user interactions with the chatbot.
  - `chatbot.py`: Contains the logic for interacting with the chatbot and generating responses.
  - `document_pipeline.py`: Handles the processing of PDF files, extracting text, and preparing data for the chatbot.
  - `requirements.txt`: A list of all the dependencies required for the project.
  - `static/`: Contains static files such as CSS and JavaScript.
    - `css/styles.css`: Stylesheet for the web application.
    - `js/scripts.js`: JavaScript file for frontend interactivity.
  - `templates/`: Contains HTML templates for the web application.
    - `index.html`: The main HTML template for the application's homepage.
  - `vector_storage.py`: Manages the storage and retrieval of vector representations of the PDF content.

- `.env`: Environment variables file.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `LICENSE`: The license file for the project.
- `README.md`: The file you are currently reading.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [Flask](https://flask.palletsprojects.com/) - A micro web framework written in Python.
- [PyPDF2](https://pypi.org/project/PyPDF2/) - A library for reading and manipulating PDF files.
- [Hugging Face](https://huggingface.co/) - A platform providing state-of-the-art natural language processing models.
