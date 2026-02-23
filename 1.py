# python 1.py

from sarvamai import SarvamAI
from dotenv import load_dotenv
import os

load_dotenv()

# Access environment variables as if they came from the actual environment
SARVAM_API_KEY = os.getenv('SARVAM_API')
client = SarvamAI(api_subscription_key=SARVAM_API_KEY)

messages = [
    {"role": "system", "content": "You are a helpful chatbot."}
]

print("Chatbot ready! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    # Example 2: Using temperature = 0.9 — more creative, varied response
    response = client.chat.completions(
        messages=messages,
        temperature=0.9  # More creative storytelling
    )

    # Receive assistant's reply as output
    bot_reply = response.choices[0].message.content
    print("Bot:", bot_reply)

    messages.append({"role": "assistant", "content": bot_reply})