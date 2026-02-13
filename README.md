# 🤖 Amixi - AI Personal Assistant from the Future

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

*Your futuristic AI assistant, available today on Telegram*

[Live Demo](#) • [Report Bug](#) • [Request Feature](#)

</div>

---

## 📖 About Amixi

**Amixi** is an advanced AI personal assistant from the year 2157, brought to life through the power of Google Gemini AI. Created by **@armevox**, Amixi combines futuristic intelligence with human warmth to help you with anything you need.

Whether you're looking for answers, solving problems, or just having a great conversation, Amixi is here to assist with a unique blend of efficiency and personality.

### ✨ Features

- 🚀 **Futuristic Personality** - Feels like chatting with an AI from the future
- 💬 **Conversational AI** - Powered by Google Gemini 1.5 Flash
- 🧠 **Memory** - Remembers your conversation within each session
- ⚡ **Fast Responses** - Quick and efficient assistance
- 🎭 **Character Consistency** - Stays in character as your helpful AI assistant
- 💰 **100% Free** - No costs, completely free to use
- ☁️ **24/7 Availability** - Deployed on Render.com

---

## 🎯 What Can Amixi Do?

- Answer questions on virtually any topic
- Help with problem-solving and decision-making
- Provide recommendations and suggestions
- Engage in creative conversations
- Assist with planning and organization
- Offer a futuristic perspective on modern challenges
- And much more!

---

## 🚀 Quick Start

### For Users

1. Open Telegram
2. Search for **@amixi_bot** (or your bot's username)
3. Press **Start**
4. Begin chatting!

### Commands

- `/start` - Introduction and welcome message
- `/reset` - Clear conversation history and start fresh

---

## 🛠️ For Developers: Deploy Your Own

Want to create your own version of Amixi? Follow these steps:

### Prerequisites

- A Telegram account
- A Google account (for Gemini API)
- A GitHub account
- A Render.com account (free)

### Step 1: Get API Keys

#### Telegram Bot Token
1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` and follow the instructions
3. Save your bot token (looks like `1234567890:ABCdefGHIjklMNO...`)

#### Google Gemini API Key
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Save your API key (starts with `AIza...`)

### Step 2: Fork & Clone

1. Fork this repository
2. Clone to your local machine (optional) or work directly on GitHub

### Step 3: Deploy to Render

1. Sign up at [Render.com](https://render.com) (use GitHub login)
2. Click "New +" → "Web Service"
3. Connect your forked repository
4. Configure:
   - **Name:** `amixi-bot` (or your choice)
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python telegram_bot_gemini.py`
   - **Instance Type:** Free

5. Add Environment Variables:
   - `TELEGRAM_BOT_TOKEN` - Your Telegram bot token
   - `GEMINI_API_KEY` - Your Google Gemini API key

6. Click "Create Web Service"
7. Wait 3-5 minutes for deployment

### Step 4: Test Your Bot

1. Open Telegram
2. Search for your bot
3. Send `/start`
4. Chat away! 🎉

---

## 🎨 Customization

Want to change Amixi's personality? Easy!

1. Open `telegram_bot_gemini.py`
2. Find the `CHARACTER_NAME` and `CHARACTER_DESCRIPTION` variables
3. Modify them to create your own unique character
4. Commit changes
5. Render will auto-deploy your updated bot

### Example Characters

```python
# A wise wizard
CHARACTER_NAME = "Merlin"
CHARACTER_DESCRIPTION = """You are Merlin, a wise and ancient wizard..."""

# A friendly robot
CHARACTER_NAME = "Robo"
CHARACTER_DESCRIPTION = """You are Robo, a cheerful robot from the year 3000..."""

# A sarcastic AI
CHARACTER_NAME = "SARA"
CHARACTER_DESCRIPTION = """You are SARA, a sarcastic AI assistant..."""
```

---

## 📁 Project Structure

```
amixi-telegram-bot/
├── telegram_bot_gemini.py  # Main bot code
├── requirements.txt        # Python dependencies
├── render.yaml            # Render deployment config
├── README.md              # This file
└── GEMINI_DEPLOYMENT_GUIDE.md  # Detailed setup guide
```

---

## 🔧 Technical Details

### Built With

- **Python 3.8+** - Programming language
- **python-telegram-bot 21.0.1** - Telegram Bot API wrapper
- **google-generativeai 0.8.3** - Google Gemini API client
- **Google Gemini 1.5 Flash** - AI model (free tier)
- **Render.com** - Cloud hosting platform

### Architecture

- **Stateless conversation management** - Each message includes conversation history
- **Async/await pattern** - Non-blocking I/O for better performance
- **Error handling** - Graceful degradation on API failures
- **Event loop management** - Compatible with various hosting platforms

---

## 📊 Free Tier Limits

### Render.com (Hosting)
- ✅ 750 hours/month runtime
- ⚠️ Instance sleeps after 15 min of inactivity
- ⚡ Wakes up on first request (~30-60 seconds)

### Google Gemini API (AI)
- ✅ 15 requests per minute
- ✅ 1,500 requests per day  
- ✅ 1 million tokens per month

*More than enough for personal use!*

---

## 🐛 Troubleshooting

### Bot doesn't respond
- Check Render logs for errors
- Verify environment variables are set correctly
- Ensure Gemini API key is valid

### "Invalid token" error
- Double-check `TELEGRAM_BOT_TOKEN` in Render
- Make sure there are no extra spaces

### Rate limit errors
- You've hit 15 requests/minute limit
- Wait a minute and try again

### Slow first response
- Normal for free tier (instance sleeping)
- Subsequent responses are instant

For more help, see [GEMINI_DEPLOYMENT_GUIDE.md](GEMINI_DEPLOYMENT_GUIDE.md)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Creator

**Created by [@armevox](https://t.me/armevox)**

A visionary innovator making futuristic AI assistance accessible to everyone.

---

## 🌟 Acknowledgments

- Thanks to [Anthropic](https://anthropic.com) for Claude (used in development)
- Thanks to [Google](https://ai.google.dev) for Gemini AI
- Thanks to [Telegram](https://telegram.org) for the Bot API
- Thanks to [Render](https://render.com) for free hosting

---

## 📞 Support

- 💬 Telegram: [@armevox](https://t.me/armevox)
- 🐛 Issues: [GitHub Issues](../../issues)
- 📧 Email: [Your email if you want to include it]

---

<div align="center">

**Made with ❤️ and AI**

*Bringing the future to you, today*

⭐ Star this repo if you found it helpful!

</div>
