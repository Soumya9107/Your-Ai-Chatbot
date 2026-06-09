const API_URL = "https://your-ai-chatbot.onrender.com";
async function sendMessage() {

    const msg = document.getElementById("message").value;

    if (!msg) return;

    const chatBox = document.getElementById("chat-box");

    // User message
    chatBox.innerHTML += `
        <div class="user">
            <div class="message">${msg}</div>
        </div>
    `;

    document.getElementById("message").value = "";

    try {

        const response = await fetch(
    `${API_URL}/chat?msg=${encodeURIComponent(msg)}`
   );

        const data = await response.json();

        // Bot response
        chatBox.innerHTML += `
            <div class="bot">
                <div class="message">${data.response}</div>
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

        // Refresh sidebar history
        loadHistory();

    } catch (error) {

        chatBox.innerHTML += `
            <div class="bot">
                <div class="message">
                    Error connecting to backend.
                </div>
            </div>
        `;
    }
}


async function loadHistory() {

    try {

        const response = await fetch(
    `${API_URL}/history`
        );

        const data = await response.json();

        const historyDiv =
            document.getElementById("history");

        historyDiv.innerHTML = "";

        data.history.forEach(chat => {

            historyDiv.innerHTML += `
                <div class="history-item">
                    <strong>You:</strong><br>
                    ${chat.user_message}
                </div>
            `;
        });

    } catch (error) {

        console.log("History loading failed");
    }
}


function toggleTheme() {

    document.body.classList.toggle("light");
}


// Enter key support
document
    .getElementById("message")
    .addEventListener("keypress", function(event) {

        if (event.key === "Enter") {
            sendMessage();
        }

    });


// Load history when page opens
loadHistory();