import subprocess



from services.UserService import *
from services.RoomService import *




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

@app.post("/room")
async def createRoom(request):
    return await RoomService.createRoom(request)

if __name__ == '__main__':

    subprocess.call(["sh", "./db/db.sh"], shell=False)
    app.run(host='0.0.0.0', port=8099, auto_reload=True)