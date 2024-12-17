import streamlit as st
import requests

# Ollama API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

# Streamlit UI Configuration
st.set_page_config(page_title="Ollama Chatbot", page_icon="🤖")
st.title("🤖 Ollama Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Function to send prompt to Ollama
def get_ollama_response(prompt):
    payload = {"model": "llama2", "prompt": prompt, "stream": False}
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error connecting to Ollama: {str(e)}"

# User Input Section
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Get Ollama response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_ollama_response(prompt)
            st.write(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
