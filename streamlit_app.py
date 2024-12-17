import streamlit as st

# Streamlit UI Configuration
st.set_page_config(page_title="Simple Chatbot", page_icon="💬")
st.title("💬 Simple Hardcoded Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Function to provide hardcoded responses
def get_hardcoded_response(prompt):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you?": "I'm just a bot, but I'm functioning as expected! How about you?",
        "bye": "Goodbye! Have a great day!",
        "what is your name?": "I'm a simple chatbot created with Streamlit.",
    }
    # Default response for unknown inputs
    return responses.get(prompt.lower(), "I'm sorry, I don't understand that.")

# User Input Section
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Get hardcoded response
    response = get_hardcoded_response(prompt)

    # Add assistant response to chat history
    with st.chat_message("assistant"):
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
