// Function to upload PDFs
function uploadFiles() {
    let files = document.getElementById("pdfUpload").files;
    if (files.length === 0) {
        document.getElementById("uploadStatus").innerText = "No file selected!";
        return;
    }

    let formData = new FormData();
    for (let i = 0; i < files.length; i++) {
        formData.append("files[]", files[i]);
    }

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("uploadStatus").innerText = data.message || data.error;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("uploadStatus").innerText = "Upload failed!";
    });
}

// Function to send message to chatbot
function sendMessage() {
    let inputField = document.getElementById("userMessage");
    let message = inputField.value.trim();
    if (message === "") return;

    // Add user message
    addMessage(message, "user");
    inputField.value = "";

    // Simulate bot response with "Processing..."
    let botMessage = addMessage("Processing...", "bot");

    // Send request to backend
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        // ✅ FIX: Extract the correct response
        if (data.response && data.response.answer) {
            botMessage.innerText = data.response.answer;  
        } else {
            botMessage.innerText = "⚠️ No valid response from chatbot!";
        }
    })
    .catch(error => {
        console.error("Error:", error);
        botMessage.innerText = "⚠️ Error retrieving response";
    });
}

// Function to add messages to chat
function addMessage(text, sender) {
    let chatBox = document.getElementById("chatBox");
    let messageDiv = document.createElement("div");
    messageDiv.classList.add("chat-message", sender);
    messageDiv.innerText = text;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
    return messageDiv;
}
