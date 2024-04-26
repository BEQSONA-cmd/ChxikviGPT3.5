import asyncio
import websockets
from json import dumps, loads
from time import sleep

from bot import bot_reply

chats = {}

def makemsg(name, message):
    return ({
        'name': name,
        'message': message
    })

def get_reply(msg):
    return f"I am not available right now {msg['name']}. Please try again later."

async def handle_message(websocket, path):
    global chats
    chat_id = int(path.split('/')[-1])
    if not chat_id in chats:
        print(f"Created new chat {chat_id}")
        chats[chat_id] = []
    chats[chat_id].append(websocket)
    async for message in websocket:
        data = loads(message)
        if chat_id in chats:
            msg = makemsg(data['name'], data['message'])
            await asyncio.wait([client.send(dumps(msg)) for client in chats[chat_id]])
            for client in chats[chat_id]:
                await client.send(dumps(makemsg('ChxikviGPT', bot_reply(*msg.values()))))
        else:
            chats[chat_id] = []

start_server = websockets.serve(handle_message, "0.0.0.0", 8880)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
