document.addEventListener("DOMContentLoaded", function () {
    const sendButton = document.getElementById("send-button");
    const messageInput = document.getElementById("message-input");
    const nameInput = document.getElementById("name-input");
    const chatIdInput = document.getElementById("chat-id-input");
    const startChatBtn = document.getElementById("start-chat-btn");
    const logoBtn = document.getElementById("logo-btn");
    const chatBox = document.getElementById("chat-box");
    const nameInputContainer = document.getElementById("name-input-container");
    const chatIdInputContainer = document.getElementById("chat-id-input-container");

    logoBtn.style.display = "none";
    chatBox.style.display = "none";
    messageInput.style.display = "none";
    sendButton.style.display = "none";

    sendButton.addEventListener("click", handleSendButtonClick);
    messageInput.addEventListener("keypress", handleKeyPress);
    nameInput.addEventListener("keypress", handleKeyPress);
    chatIdInput.addEventListener("keypress", handleKeyPress);
    startChatBtn.addEventListener("click", startChat);

    function handleSendButtonClick() {
        sendMessage(messageInput.value.trim());
    }

    let ws;

    function sendMessage(message) {
        if (ws.readyState === WebSocket.OPEN) {
            ws.send(JSON.stringify({
                name: nameInput.value.trim(),
                chatId: chatIdInput.value.trim(),
                message: message
            }));
            messageInput.value = "";
        }
    }

    function handleKeyPress(event) {
        if (event.key === "Enter") {
            if (event.target === messageInput) {
                sendMessage(messageInput.value.trim());
            } else {
                startChat();
            }
        }
    }

    async function startChat() {
        const name = nameInput.value.trim();
        const chatId = chatIdInput.value.trim();

        if (name !== "" && chatId !== "") {
            nameInputContainer.style.display = "none";
            chatIdInputContainer.style.display = "none";
            startChatBtn.style.display = "none";

            logoBtn.style.display = "block";
            chatBox.style.display = "block";
            messageInput.style.display = "block";
            sendButton.style.display = "block";

            ws = new WebSocket(`ws://132.145.250.27:8880/chat/${chatId}`);

            ws.onmessage = function (event) {
                const data = JSON.parse(event.data);
                const messageElement = document.createElement("div");
                messageElement.textContent = `${data.name}: ${data.message}`;
                chatBox.appendChild(messageElement);
                chatBox.scrollTop = chatBox.scrollHeight;
            }
        } else {
            alert("Please enter your name.");
        }
    }
});
