from ipaddress import ip_address
from websockets import serve
from utilities import get_king, set_king, get_websocket_info
import asyncio


async def main(address):
    async with serve(handler, address[0], int(address[1])):
        await asyncio.Future()  # run forever


async def handler(websocket):
    async for message in websocket:
        message_list = message.split("-|\\|-")
        if message.lower() == "ping":
            websocket.send("pong")
        elif message_list[0] == "setKing":
            if message_list[1] != get_king():
                set_king(message_list[1])
                websocket.send("Already king")
            else:    
                websocket.send("Success")


asyncio.run(main(get_websocket_info()))