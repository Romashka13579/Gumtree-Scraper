import telegram
bot = telegram.Bot(token='7216096099:AAFN-2lH6-IAjVhdhDk5MXJy75p8KFsXiKg')

async def send_message(text, chat_id):
    async with bot:
        await bot.send_message(text=text, chat_id=chat_id)

async def main():
    
    await send_message(text='', chat_id='984091159')


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())