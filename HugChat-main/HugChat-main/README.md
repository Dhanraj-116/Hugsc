# 🤖 HugChat – Hugging Face Chatbot with Gradio

HugChat is a simple yet powerful chatbot built using Hugging Face's Zephyr model and Gradio.  
It supports natural conversation via a clean web interface and is easily customizable for various use-cases like personal assistants, helpdesk bots, or educational tools.

---

## 🚀 Features

- 💬 Conversational UI powered by [Gradio](https://www.gradio.app/)
- 🔗 Uses Hugging Face Inference API (`zephyr-7b-beta` model)
- 🔐 Secure API access via `.env`
- 🎨 Simple, styled chat interface

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/Arlahanmanthrao1/HugChat.git
cd HugChat
📦 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🛡️ 3. Create a .env File
Create a .env file in the root of your project directory and add your Hugging Face API token:

env
Copy
Edit
HF_TOKEN=your_huggingface_api_token
🔑 You can get your Hugging Face token from: https://huggingface.co/settings/tokens

▶️ Run the App
bash
Copy
Edit
python chatbot_app.py
Then open your browser and visit:
http://127.0.0.1:7860

