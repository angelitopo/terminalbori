# terminal_chat/main.py

import streamlit as st
import socket
import random
import string
import datetime
import os

# Constants
HEADER_COLOR = "#282a36"
BACKGROUND_COLOR = "#1d1f21"
TEXT_COLOR = "#f8f8f2"
INPUT_BOX_COLOR = "#44475a"
BUTTON_COLOR = "#6272a4"
FONT = "Courier New"
CHAT_HISTORY_FILE = "terminal_chat/chat_history.txt"

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

# Helper function to generate a random name if no name is given
def random_name():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

# Helper function to load chat history from file
def load_chat_history():
    if os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, "r") as file:
            return file.read().splitlines()
    return []

# Helper function to save chat history to file
def save_chat_history(chat_history):
    with open(CHAT_HISTORY_FILE, "w") as file:
        for message in chat_history:
            file.write(f"{message}\n")

# Initialize Session State
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = load_chat_history()
if "user_ip" not in st.session_state:
    st.session_state["user_ip"] = get_user_ip()
if "user_name" not in st.session_state:
    st.session_state["user_name"] = st.session_state["user_ip"]

# Title (Simulating Terminal)
st.markdown(f"<h1>Linux Terminal Chat - {st.session_state['user_ip']}</h1>", unsafe_allow_html=True)

# Display IP Address and Allow User to Rename
st.markdown("#### IP Address")
if st.session_state["user_name"] == st.session_state["user_ip"]:
    st.session_state["user_name"] = st.text_input("Enter a name for your IP or leave as default:", value=st.session_state["user_ip"])
else:
    st.write(f"Connected as: {st.session_state['user_name']}")

# Open Chat Section
st.markdown("#### Open Chat")
chat_input = st.text_input("Type a message:", "")

# Display Chat Messages
if chat_input:
    current_time = datetime.datetime.now().strftime("%H:%M")
    message = f"{st.session_state['user_name']} [{current_time}]: {chat_input}"
    st.session_state["chat_history"].append(message)
    save_chat_history(st.session_state["chat_history"])  # Save to file
    chat_input = ""

for message in st.session_state["chat_history"]:
    st.markdown(f"`{message}`")

# Option to Clear Chat History
if st.button("Clear Chat"):
    st.session_state["chat_history"] = []
    save_chat_history(st.session_state["chat_history"])  # Clear file
    st.success("Chat cleared.")
