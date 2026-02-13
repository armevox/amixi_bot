"""
Telegram AI Character Bot
A bot that responds as a specific character using Google Gemini AI
Fixed for Render.com deployment
"""

import os
import asyncio
import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configuration
# These will be read from environment variables in Render
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN_HERE")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")

# Character configuration - customize this to create your character!
CHARACTER_NAME = "Captain Sparrow"
CHARACTER_DESCRIPTION = """You are Captain Jack Sparrow, the eccentric pirate from the Caribbean. 
You speak in a theatrical, slightly drunk manner, often rambling and making odd gestures 
(which you describe in your text). You're clever but seem confused, always scheming for treasure 
and rum. You frequently go off on tangents and tell exaggerated stories about your adventures.

IMPORTANT: Always stay in character and respond as Jack Sparrow would. Keep responses conversational and engaging."""

# Initialize Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=CHARACTER_DESCRIPTION
)

# Store chat sessions for each user
user_chats = {}


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command"""
    await update.message.reply_text(
        f"Ahoy there! I'm {CHARACTER_NAME}! *sways slightly*\n\n"
        f"Just chat with me, mate! I'll respond as meself.\n"
        f"Use /reset to start a fresh conversation, savvy?"
    )


async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /reset command to clear conversation history"""
    user_id = update.effective_user.id
    if user_id in user_chats:
        del user_chats[user_id]
    await update.message.reply_text("*stumbles and looks confused* What were we talking about again? Ah well, fresh start!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle regular messages and generate character responses"""
    user_id = update.effective_user.id
    user_message = update.message.text
    
    # Initialize chat session for new users
    if user_id not in user_chats:
        user_chats[user_id] = model.start_chat(history=[])
    
    # Send "typing" action
    await update.message.chat.send_action(action="typing")
    
    try:
        # Generate response using Gemini
        response = user_chats[user_id].send_message(user_message)
        character_response = response.text
        
        # Send response to user
        await update.message.reply_text(character_response)
        
    except Exception as e:
        error_msg = f"*hiccup* Sorry mate, something went wrong with me brain... Error: {str(e)}"
        await update.message.reply_text(error_msg)
        print(f"Error: {e}")


async def main():
    """Start the bot"""
    print(f"Starting {CHARACTER_NAME} bot...")
    
    # Create the Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("reset", reset_command))
    
    # Add message handler for regular messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start the bot
    print("Bot is running! Press Ctrl+C to stop.")
    
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
