import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context):
    await update.message.reply_text(
        "👋 Welcome to ReelsDownloader Bot!\n\nSend me any Instagram Reel link."
    )

async def handle_message(update: Update, context):
    text = update.message.text

    if "instagram.com/reel" in text:
        link = f"https://reelsdownloader.xyz/?url={text}"
        await update.message.reply_text(f"✅ Download here:\n{link}")
    else:
        await update.message.reply_text("❌ Please send a valid Instagram Reel link.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))
print("✅ Bot started successfully...")

app.run_polling()
