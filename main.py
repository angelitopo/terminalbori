# terminal_chat/main.py

import streamlit as st
import socket
import datetime

# Constants for styling
HEADER_COLOR = "#282a36"
BACKGROUND_COLOR = "#1d1f21"
TEXT_COLOR = "#f8f8f2"
INPUT_BOX_COLOR = "#44475a"
BUTTON_COLOR = "#6272a4"
FONT = "Courier New"

# Streamlit Page Configurations
st.set_page_config(page_title="Linux Terminal Chat", layout="centered", initial_sidebar_state="collapsed")

# CSS Styling for Terminal Look
st.markdown(f"""
    <style>
        .main {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
            font-family: {FONT};
        }}
        .stTextInput > div > div {{
            background-color: {INPUT_BOX_COLOR};
        }}
        .stButton > button {{
            background-color: {BUTTON_COLOR};
            color: white;
            font-size: 14px;
            font-family: {FONT};
        }}
        h1 {{
            color: {TEXT_COLOR};
            font-family: {FONT};
        }}
    </style>
""", unsafe_allow_html=True)

# Helper function to get the user's IP address
def get_user_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Display IP address and allow the user to rename it
user_ip = get_user_ip()
st.markdown(f"<h1>Linux Terminal Chat - {user_ip}</h1>", unsafe_allow_html=True)
user_name = st.text_input("Enter a name for your IP or leave as default:", value=user_ip)

# Chat input
st.markdown("#### Open Chat")
chat_input = st.text_input("Type a message:")

# Button to send chat message
if st.button("Send Message") and chat_input:
    current_time = datetime.datetime.now().strftime("%H:%M")
    message = f"{user_name} [{current_time}]: {chat_input}"
    # Send message via Gun.js (JavaScript code below will handle this)

# Inject Gun.js and JavaScript code for real-time chat management
st.markdown(f"""
    <script src="https://cdn.jsdelivr.net/npm/gun/gun.min.js"></script>
    <script>
        // Initialize Gun.js
        const gun = Gun();

        // Store the chat data
        const chat = gun.get("terminal-chat");

        // Display existing messages and listen for new ones
        chat.map().on((message, id) => {{
            const chatContainer = document.getElementById("chat-container");
            if (chatContainer) {{
                const messageElement = document.createElement("div");
                messageElement.style.color = "{TEXT_COLOR}";
                messageElement.style.fontFamily = "{FONT}";
                messageElement.style.margin = "5px 0";
                messageElement.textContent = message;
                chatContainer.appendChild(messageElement);
                chatContainer.scrollTop = chatContainer.scrollHeight;  // Auto-scroll to the latest message
            }}
        }});

        // Send a new message
        function sendMessage() {{
            const input = document.getElementById("chat-input");
            if (input && input.value) {{
                const timestamp = new Date().toLocaleTimeString();
                const userMessage = "{user_name}" + " [" + timestamp + "]: " + input.value;
                chat.set(userMessage);  // Store message in Gun.js
                input.value = "";  // Clear input field
            }}
        }}
    </script>

    <!-- Chat Display Area -->
    <div id="chat-container" style="background-color: {BACKGROUND_COLOR}; padding: 10px; border-radius: 5px; height: 300px; overflow-y: auto; border: 1px solid {BUTTON_COLOR};">
        <!-- Messages will appear here -->
    </div>

    <!-- Input and Button for Chat -->
    <input id="chat-input" type="text" placeholder="Type a message..." style="width: 80%; padding: 5px; border-radius: 5px; border: 1px solid {INPUT_BOX_COLOR}; background-color: {INPUT_BOX_COLOR}; color: {TEXT_COLOR}; font-family: {FONT};">
    <button onclick="sendMessage()" style="padding: 5px 10px; margin-left: 5px; border: none; border-radius: 5px; background-color: {BUTTON_COLOR}; color: white; font-family: {FONT}; cursor: pointer;">Send</button>
""", unsafe_allow_html=True)
