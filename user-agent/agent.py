from pyrogram import Client, filters, types
from .classifer import classifier

API_ID = 25652534
API_HASH = '9787c9f77cfb0182c002ea94c4073e73'
CHANNEL_ID = '-1001275637856'

if not API_HASH or API_ID == 1234:
    print("my.telegram.org dan olgan ma'lumotlaringizni kiriting")
    API_ID = input("API_ID: ")
    API_HASH = input("API_HASH: ")

app = Client("userbot2", API_ID, API_HASH)


@app.on_message(filters.channel)
async def nb_command(_, msg: types.Message):

    result = classifier(msg.text)
    if result[1] > 70:
        await msg.copy(973108256)



@app.on_message(filters.private)
async def join(_, msg: types.Message):
    if msg.text.startswith('join '):
        username = msg.text.split(' ')[1]
        await app.join_chat(username)
        await msg.reply_text(f"Joined to {username}")


# @app.on_message(filters.channel)
# async def nb_command(_, msg: types.Message):
#     pass
    # if msg.chat.id == CHANNEL_ID:
    # if msg.text 
        # await msg.copy('@Jonibek_Yorqulov')
    # await msg.copy(973108256)
    # await msg.forward(973108256)

# @app.on_message(filters.me & filters.command("nb", prefixes=[".", "!"]))
# async def nb_command(_, msg: types.Message):
#     await msg.edit_text(TEXT)
    
    

app.run()