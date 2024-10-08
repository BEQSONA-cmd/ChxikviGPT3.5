#!/usr/bin/env python3
import asyncio
import websockets
from json import dumps, loads
from time import sleep
# from bot import bot_reply

def gethost():
    from socket import gethostname
    if gethostname().endswith('42wolfsburg.de'):
        return 'localhost'
    return 'localhost' # YOUR_IP_ADDRESS should be replaced with the IP address of the machine where the server is running

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
        chats[chat_id] = set()
    chats[chat_id].add(websocket)
    try:
        async for message in websocket:
            data = loads(message)
            if chat_id in chats:
                msg = makemsg(data['name'], data['message'])
                tasks = [client.send(dumps(msg)) for client in chats[chat_id]]
                await asyncio.wait([asyncio.create_task(task) for task in tasks])
                await asyncio.sleep(1)
                # response = bot_reply(*msg.values())
                # for client in chats[chat_id]:
                #     await client.send(dumps(makemsg('ChxikviGPT', response)))
            else:
                chats[chat_id] = set()
    finally:
        if chat_id in chats:
            chats[chat_id].remove(websocket)

start_server = websockets.serve(handle_message, gethost(), 8880)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

