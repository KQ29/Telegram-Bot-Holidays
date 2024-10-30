# 🤖 AI Chatbot

Welcome to the AI Chatbot project! This chatbot is powered by **Telegram** and **Hugging Face** AI models, providing smart, human-like responses to messages. Perfect for adding conversational AI to your Telegram bot or experimenting with AI-driven interactions!

## 📂 Project Structure

- **main.py**: 🎛️ This is the bot’s main control file, where the bot is initialized, message handling is defined, and responses are managed.
- **chatbot_AI.py**: 🧠 The brain of the chatbot! Contains AI response logic using Hugging Face’s Inference API.
- **requirements.txt**: 📦 A list of dependencies required for the project to run smoothly.
- **Procfile**: 📄 Configuration for deployment (suitable for platforms like Heroku).
- **.gitignore**: 🚫 Excludes unnecessary files, such as virtual environments, cached files, and configuration files containing sensitive information.

## ✨ Features

- **AI-Powered Responses**: Delivers interactive, human-like responses using a Hugging Face model.
- **Error Handling**: Ensures seamless interaction with user-friendly messages if errors occur.
- **Customizable Prompts**: Adjust the bot's tone and style with custom prompts.
- **Telegram Integration**: Connects easily with Telegram to handle user messages and provide replies.

## 🚀 Getting Started

### ✅ Prerequisites

1. **Python 3.8+** is required for compatibility.
2. Install project dependencies with:
    
   ```bash
   pip install -r requirements.txt
   ```
   
## 🔐 Environment Setup
### API Keys:
#### Obtain your Hugging Face API key and Telegram bot token.
#### Environment Variables:
#### Create a config.py file at the project root.
#### Inside config.py, define:

- **BOT_TOKEN** = 'your-telegram-bot-token'
- **API_Key** = 'your-hugging-face-api-key'

## 🏃 Running the Bot
### To start the bot on your local machine, simply run:

```bash
python main.py
```

Alternatively, for deployment on platforms that support Procfile (like Heroku), follow these steps to deploy the bot to the cloud.

## 🛠️ Configuration
#### The bot uses the Hugging Face tiiuae/falcon-7b-instruct model for response generation. You can customize the model settings by adjusting the parameters in chatbot_AI.py. Here’s a quick guide:

- **max_new_tokens**: Controls response length.
- **temperature**: Adjusts creativity; higher values yield more diverse responses.
- **top_p**: Controls the range of vocabulary for response selection.
### Example of generating a response:

   ```bash
response = client.text_generation(
    prompt="Hello, how can I help you?",
    max_new_tokens=150,
    temperature=0.85,
    top_p=0.9
)
 ```

## 🤖 Response Management
### The AI response is refined to keep the conversation smooth:

The response generator removes unnecessary labels and formatting.
If the response is empty or unclear, a friendly default message is sent to keep the user engaged.

## 🧩 Example Usage
### To try out the chatbot:

- **Start a conversation**: Message the bot on Telegram.
- **Chat**: Type in any message; the bot will respond based on the AI model’s output.
- **Error-Free Communication**: The bot gracefully handles errors and logs them for easy troubleshooting.

## 🛠️ Deployment
- **Procfile**: Ensure that your deployment platform supports Procfiles.
- **Example**: worker: python main.py will start the bot automatically.
- **Secure API Management**: Make sure API keys are securely managed (e.g., using environment variables).

## ⚙️ Project Dependencies
### The bot relies on several Python packages:

- **aiogram**: Handles Telegram interactions.
- **huggingface_hub**: Connects to the Hugging Face API for AI model integration.
- **python-dotenv**: Manages environment variables for secure API key storage.

### To install all dependencies, run:

```bash
pip install -r requirements.txt
```

## 📝 License
This project is licensed under the MIT License.
