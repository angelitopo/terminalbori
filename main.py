# terminal_chat/main.py

import streamlit as st
import socket
import random
import string
import datetime

# Constants
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

# Helper function to generate a random name if no name is given
def random_name():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

# Initialize Session State
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
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
    st.session_state["chat_history"].append(f"{st.session_state['user_name']} [{current_time}]: {chat_input}")
    chat_input = ""

for message in st.session_state["chat_history"]:
    st.markdown(f"`{message}`")

# Option to Clear Chat History
if st.button("Clear Chat"):
    st.session_state["chat_history"] = []
    st.success("Chat cleared.")
