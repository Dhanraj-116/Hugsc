import gradio as gr
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# ✅ Load .env file
load_dotenv()

# ✅ Get token from environment
api_key = os.getenv("HF_TOKEN")

client = InferenceClient(
    provider="hf-inference",
    api_key=api_key,
)

chat_history = []

def chatbot_fn(user_message, history=[]):
    global chat_history
    chat_history.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions.create(
            model="HuggingFaceH4/zephyr-7b-beta",
            messages=chat_history,
        )
        bot_message = response.choices[0].message.content.strip()
        chat_history.append({"role": "assistant", "content": bot_message})
        return bot_message
    except Exception as e:
        return f"❌ Error: {str(e)}"

gr.ChatInterface(fn=chatbot_fn, title="🤖 Hugging Face Chatbot", theme="soft").launch()
