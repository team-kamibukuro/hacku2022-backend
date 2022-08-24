import subprocess
from sanic_cors.extension import CORS
from sanic_ext import Extend


from services.UserService import *
from services.RoomService import *
from services.ws.WsService import *
from services.ConsoleService import *




app = Sanic("HackU2022-backend")
app.config.CORS_ORIGINS = "http://localhost:3000"
Extend(app)


@app.get("/")
async def hello_world(request):
    return response.json({"massage": "Hello World !!"})


@app.post("/signup")
async def signup(request):
    return await UserService.userSignup(request)

@app.post("/login")
async def login(request):
    return await UserService.userLogin(request)

@app.post("/room")
async def createRoom(request):
    return await RoomService.createRoom(request)

@app.post("/room/get")
async def getRoom(request):
    return await RoomService.getRoom(request)

@app.post("/room/matching")
async def getMatchingRoom(request):
    return await RoomService.getMatchingRoom(request)

@app.post("/console")
async def executeConsole(request):
    return await ConsoleService.getConsoleResult(request)

@app.post("/testcase")
async def executeTestCase(request):
    return await ConsoleService.getTestCaseResult(request)





@app.websocket("/play/<room_id>")
async def playGame(request,  ws, room_id):
    return await WsService.playGame(request,  ws, room_id)





if __name__ == '__main__':

    # subprocess.call(["sh", "./init_db/db.sh"], shell=False)
    app.run(host='127.0.0.1', port=80, auto_reload=True)