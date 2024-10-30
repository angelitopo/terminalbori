#!/bin/bash
# setup.sh - Script to set up the environment

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run terminal_chat/main.py
