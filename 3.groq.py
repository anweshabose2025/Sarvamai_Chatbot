# streamlit run 3.groq.py

import streamlit as st
from openai import OpenAI

# ---- CONFIG ----
st.set_page_config("🤖 OpenAI")
st.sidebar.title("Settings")
groq_api_key=st.sidebar.text_input("Enter your Groq API Key:",type="password")
model=st.sidebar.selectbox("Select Open Source model",["openai/gpt-oss-120b","openai/gpt-oss-20b"])
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.2) # value=0.2: default temperature

if not groq_api_key:
    st.warning("⚠️ Please enter the Groq API Key before you proceed...")

st.title("OpenAI Chat Playground", text_alignment = "center")

client = OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",
)

# Initialize chat history
if "messages" not in st.session_state:
    #st.subheader("What are you working on?", text_alignment = "center")
    #st.divider()
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful chatbot."}
    ]

if len(st.session_state.messages) == 1:
    st.subheader("What are you working on?", text_alignment = "center")
    st.divider()
    
# Show previous chat messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input box
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call OpenAI
    response = client.responses.create(
        input=st.session_state.messages,
        model=model
    )

    bot_reply = response.output_text

    # Show assistant message
    with st.chat_message("assistant"):
        st.write(bot_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )