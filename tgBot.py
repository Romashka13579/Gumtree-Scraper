# bot token = 7216096099:AAFN-2lH6-IAjVhdhDk5MXJy75p8KFsXiKg

from typing import final
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, ContextTypes, ApplicationBuilder

token: final = '7216096099:AAFN-2lH6-IAjVhdhDk5MXJy75p8KFsXiKg'
botname: final = '@scrapic_from_scrap_bot'

async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello")

async def stop_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am scrapic')

async def main():
    
    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("stop", stop_command))

    await application.initialize()

    await application.run_polling(poll_interval=3)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())