
from sanic import Sanic
from sanic import response
from app.main import app


@app.get("/")
async def hello_world(request):
    return response.json({"massage": "Hello World !!"})


