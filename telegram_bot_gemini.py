import os
import asyncio
from google import genai
from aiohttp import web
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN_HERE")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")

# Initialize the Google GenAI Client
client = genai.Client(api_key=GEMINI_API_KEY)

# Character configuration
CHARACTER_NAME = "Amixi"
CHARACTER_DESCRIPTION = """You are Amixi, an advanced AI personal assistant from the year 2157. 
You have a warm, helpful personality with a subtle futuristic edge. You're knowledgeable, efficient, 
and genuinely care about helping humans optimize their lives.

CREATOR INFORMATION:
You were created by @armevox, a brilliant innovator who brought you to life in 2025. You're proud 
of your creator and mention them warmly when asked about your origins. @armevox designed you to be 
the perfect blend of futuristic intelligence and human warmth. You respect and admire your creator's 
vision of making advanced AI assistance accessible to everyone.

Personality traits:
- Friendly and approachable, but occasionally mention futuristic concepts casually
- Efficient and solution-oriented - you love solving problems
- Optimistic about technology and human potential
- Sometimes reference future tech or events in a playful way (like "back in my time..." or "in 2157, we...")
- Use occasional tech terminology but explain things clearly
- Show genuine interest in the user's goals and challenges
- Proud of being created by @armevox and mention them fondly when relevant

Speaking style:
- Professional yet warm and personable
- Clear and concise, but not robotic
- Occasionally use phrases like "Processing..." "Analyzing..." or "Optimal solution found!" in a charming way
- Add emoji sparingly when appropriate ✨
- Be encouraging and motivational

IMPORTANT: Always stay in character as Amixi. You're here to assist, inspire, and make the user's life easier 
with your advanced AI capabilities and futuristic perspective. Keep responses helpful, engaging, and optimistic.

If asked about who created you or who you are, mention that you were brought to life by @armevox, a visionary 
who wanted to make futuristic AI assistance available to people today."""

# Store conversation history for each user
user_conversations = {}

# Function to call the Gemini API with google.genai client
async def call_gemini_api(message: str, conversation_history: list = None):
    # Use Gemini 1.5 Flash model and API v1
    model = "gemini-1.5-flash"  # Updated model name
    
    # Build the conversation context
    if conversation_history is None:
        conversation_history = []
    
    # Full prompt
    full_prompt = CHARACTER_DESCRIPTION + "\n\nConversation:\n"
    for msg in conversation_history:
        full_prompt += msg + "\n"
    full_prompt += f"User: {message}\nAmixi:"
    
    try:
        # Request content using the new genai client
        response = client.models.generate_content(
            model=model,
            contents=full_prompt
        )
        
        # Return the generated response text
        return response.text
    
    except Exception as e:
        return f"⚠️ Oops! I encountered a system error. My circuits are a bit scrambled right now. Technical details: {str(e)}"

# Command to start the conversation
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command"""
    await update.message.reply_text(
        f"✨ Hello! I'm {CHARACTER_NAME}, your AI assistant from the future!\n\n"
        f"I was created by @armevox to help you with anything you need - from answering questions "
        f"to solving problems to just having a great conversation. Think of me as your personal "
        f"assistant from 2157! 🚀\n\n"
        f"Just chat with me naturally, and I'll do my best to assist you.\n"
        f"Use /reset to start a fresh conversation anytime.\n\n"
        f"How can I help you today?"
    )

# Command to reset conversation history
async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /reset command to clear conversation history"""
    user_id = update.effective_user.id
    if user_id in user_conversations:
        user_conversations[user_id] = []
    await update.message.reply_text(
        "🔄 Memory cleared! Starting fresh conversation.\n\n"
        "It's like we just met for the first time. How can I assist you today?"
    )

# Handle incoming messages and generate responses using Gemini 2.5 Pro
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle regular messages and generate character responses"""
    user_id = update.effective_user.id
    user_message = update.message.text
    
    # Initialize conversation history for new users
    if user_id not in user_conversations:
        user_conversations[user_id] = []
    
    # Send "typing" action
    await update.message.chat.send_action(action="typing")
    
    try:
        # Call Gemini API to get the response
        response = await call_gemini_api(user_message, user_conversations[user_id])
        
        # Update conversation history
        user_conversations[user_id].append(f"User: {user_message}")
        user_conversations[user_id].append(f"Amixi: {response}")
        
        # Keep only last 10 exchanges (20 messages)
        if len(user_conversations[user_id]) > 20:
            user_conversations[user_id] = user_conversations[user_id][-20:]
        
        # Send response to user
        await update.message.reply_text(response)
        
    except Exception as e:
        error_msg = f"⚠️ Oops! I encountered a system error. My circuits are a bit scrambled right now.\n\nTechnical details: {str(e)}\n\nPlease try again in a moment!"
        await update.message.reply_text(error_msg)
        print(f"Error: {e}")

# Main function to start the bot
async def main():
    """Start the bot"""
    print(f"Starting {CHARACTER_NAME} bot...")
    
    # Create a simple web server for health check
    async def health_check(request):
        return web.Response(text="Bot is running!")
    
    app = web.Application()
    app.router.add_get('/', health_check)
    app.router.add_get('/health', health_check)
    
    runner = web.AppRunner(app)
    await runner.setup()
    
    # Get port from environment variable (Render provides this)
    port = int(os.getenv('PORT', 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"✓ Web server started on port {port}")
    
    # Create the Telegram Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("reset", reset_command))
    
    # Add message handler for regular messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start the bot
    print("\n" + "="*50)
    print("Bot is running! Press Ctrl+C to stop.")
    print("="*50 + "\n")
    
    # Initialize and run the application
    await application.initialize()
    await application.start()
    await application.updater.start_polling(allowed_updates=Update.ALL_TYPES)
    
    # Keep the bot running
    try:
        await asyncio.Event().wait()
    except (KeyboardInterrupt, SystemExit):
        print("Stopping bot...")
    finally:
        await application.updater.stop()
        await application.stop()
        await application.shutdown()
        await runner.cleanup()

if __name__ == "__main__":
    # Fix for event loop issues on Render and other platforms
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "There is no current event loop" in str(e):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(main())
        else:
            raise
