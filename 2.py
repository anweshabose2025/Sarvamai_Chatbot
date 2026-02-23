# streamlit run 2.py

import streamlit as st
from sarvamai import SarvamAI

# ---- CONFIG ----
st.set_page_config("🤖 SarvamAI")
st.sidebar.title("Settings")
sarvam_api_key=st.sidebar.text_input("Enter your SarvamAI API Key:",type="password")
model=st.sidebar.selectbox("Open Source model (by default)",["sarvam-m"])
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.9) # value=0.2: default temperature

if not sarvam_api_key:
    st.warning("⚠️ Please enter the Sarvam API Key before you proceed...")

st.title("SarvamAI Chat Playground", text_alignment = "center")

client = SarvamAI(api_subscription_key=sarvam_api_key)

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

    # Call SarvamAI
    response = client.chat.completions(
        messages=st.session_state.messages,
        temperature=temperature
    )

    bot_reply = response.choices[0].message.content

    # Show assistant message
    with st.chat_message("assistant"):
        st.write(bot_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )