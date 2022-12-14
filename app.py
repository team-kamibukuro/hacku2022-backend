import subprocess
from sanic_cors.extension import CORS
from sanic_ext import Extend



from services.UserService import *
from services.RoomService import *
from services.ws.WsService import *
from services.ConsoleService import *
from services.MyPageService import *




app = Sanic("HackU2022-backend")
app.config.CORS_ORIGINS = "http://localhost:3000"
app.config.CORS_ORIGINS = "https://injection-game.vercel.app/"
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

@app.get("/mypage/<userId>")
async def executeTestCase(request, userId):
    return await MyPageService.getMyPage(request, userId)

@app.get("/match-history/<userId>")
async def executeTestCase(request, userId):
    return await MyPageService.getMatchHistory(request, userId)

@app.get("/match-history/<userId>/<roomId>")
async def executeTestCase(request, userId, roomId):
    return await MyPageService.getMatchHistoryDetail(request, userId, roomId)



@app.websocket("/play/<room_id>")
async def playGame(request,  ws, room_id):
    return await WsService.playGame(request,  ws, room_id)



subprocess.call(["sh", "./init_db/db.sh"], shell=False)

if __name__ == '__main__':


    app.run(host='0.0.0.0', port=8099, auto_reload=True)