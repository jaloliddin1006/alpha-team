from pyrogram import Client, filters, types
from classifer import classifier
from save_db import save_vacancy
import os

# API_ID = os.getenv("API_ID")
# API_HASH = os.getenv("API_HASH")

API_ID=25652534
API_HASH='9787c9f77cfb0182c002ea94c4073e73'


if not API_HASH or API_ID == 1234:
    print("my.telegram.org dan olgan ma'lumotlaringizni kiriting")
    API_ID = input("API_ID: ")
    API_HASH = input("API_HASH: ")

app = Client("userbot2", API_ID, API_HASH)


@app.on_message(filters.channel)
async def nb_command(_, msg: types.Message):

    category = classifier(msg.text)
    link = msg.link
    if len(msg.text) > 70:
        save_vacancy( category, link)
        await app.send_message(973108256, f"yangi ish qo'shildi: {category}  |  {link}")
        # await msg.copy(973108256)



@app.on_message(filters.private)
async def join(_, msg: types.Message):
    if msg.text.startswith('join '):
        username = msg.text.split(' ')[1]
        await app.join_chat(username)
        await msg.reply_text(f"Joined to {username}")



app.run()