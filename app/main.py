import sys

sys.path.append('./models')
sys.path.append('./repository')
sys.path.append('./services')
print(sys.path)


import subprocess


from sanic import Sanic
from sanic import response
from services.UserService import *

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


@app.post("/signup")
async def signup(request):
    return await UserService.userSignup(request)

@app.post("/login")
async def login(request):
    return await UserService.userLogin(request)

if __name__ == '__main__':

    subprocess.call(["sh", "./db/db.sh"], shell=False)
    app.run(host='0.0.0.0', port=8099, auto_reload=True)