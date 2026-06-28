import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Get the bot token from environment variables
TOKEN = os.environ.get("TELEGRAM_TOKEN")

async def start(update, context):
    await update.message.reply_text("Hi! Send me a prompt to generate an image!")

async def handle_message(update, context):
    prompt = update.message.text
    # TODO: Call your chosen AI API here
    # image = generate_image(prompt)
    # await update.message.reply_photo(image)
    await update.message.reply_text(f"Generating image for: {prompt}...")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    print("Starting bot with long polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
