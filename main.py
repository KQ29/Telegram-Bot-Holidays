import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from config import BOT_TOKEN
from chatbot_AI import generate_response  # Import the AI response function

# Suppress the tokenizer parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():

    # Initialize the bot and dispatcher
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Get the bot's user ID
    bot_info = await bot.get_me()
    bot_id = bot_info.id

    # Define a message handler that generates AI responses
    @dp.message()
    async def handle_message(message: types.Message):
        # Ignore messages sent by the bot itself
        if message.from_user.id == bot_id:
            return

        user_text = message.text
        try:
            ai_response = generate_response(user_text)  # Get AI-generated response
            # Check if the response is empty and provide a default message if needed
            if not ai_response.strip():
                ai_response = "I'm sorry, I couldn't generate a response right now. Please try again."
            await message.answer(ai_response)  # Send response back to the user
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            await message.answer("Sorry, there was an error processing your request.")

    # Start polling
    logger.info("Starting bot polling...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
