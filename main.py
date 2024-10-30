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

# Initialize shared chat history if not already set
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Display IP address and allow the user to rename it
user_ip = get_user_ip()
st.markdown(f"<h1>Linux Terminal Chat - {user_ip}</h1>", unsafe_allow_html=True)
user_name = st.text_input("Enter a name for your IP or leave as default:", value=user_ip)

# Chat input
st.markdown("#### Open Chat")
chat_input = st.text_input("Type a message:")

# Button to submit the chat message
if st.button("Send Message"):
    if chat_input:
        current_time = datetime.datetime.now().strftime("%H:%M")
        message = f"{user_name} [{current_time}]: {chat_input}"
        st.session_state["chat_history"].append(message)  # Append to shared chat history

# Display chat messages
for message in st.session_state["chat_history"]:
    st.markdown(f"`{message}`")

# Clear chat history
if st.button("Clear Chat"):
    st.session_state["chat_history"].clear()  # Clear chat history for all users
