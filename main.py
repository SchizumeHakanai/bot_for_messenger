from fbchat_muqit import Client, Message, ThreadType
import asyncio
import sys
import random

COOKIES_FILE="cookies.json"
PREFIX="!"

class BotMessenger(Client):
    async def onMessage(self, mid, author_id: str, message_object: Message, thread_id, thread_type=ThreadType.USER, **kwargs):
        if author_id == self.uid:
            return
        text = message_object.text or " "
        if not text.startswith(PREFIX):
            return

        cmd = message_object.text
        if cmd == "!test":
            await message_object.reply("To jest testowa komenda")

        if cmd == "!losuj":
            cm = random.randint(1, 90)
            await message_object.reply(f"Wylosowana liczba {cm}!")



async def main():
    bot = await BotMessenger.startSession(COOKIES_FILE)
    if await bot.isLoggedIn():
        fetch_client_info = await bot.fetchUserInfo(bot.uid)
        client_info = fetch_client_info[bot.uid]
        print("Online: " + client_info.name)

    try:
        await bot.listen()
    except Exception as e:
        print(e)

# Are you using Windows? Uncomment these two lines.
if sys.platform.startswith("win"):
   asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
