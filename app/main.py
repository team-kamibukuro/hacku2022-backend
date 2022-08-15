import subprocess

from sanic.response import json
from sanic import Sanic
from sanic import response

from sqlalchemy.ext.declarative import declarative_base

import binascii
import uuid
import json

from sanic.response import text

from sanic.log import logger


from sanic.server.websockets.impl import WebsocketImplProtocol as Websocket





app = Sanic("HackU2022-backend")

@app.get("/")
async def hello_world(request):
    return response.json({"massage": "Hello World !!"})


@app.get("/siginup")
async def siginup(request):
    return response.json({"massage": "Hello World !!"})

if __name__ == '__main__':
    subprocess.call(["sh", "./db/db.sh"], shell=False)
    app.run(host='0.0.0.0', port=8099, auto_reload=True)