from sanic import Sanic
from sanic import response
from models.User import User
from .clientJwt import *
import json
from sqlalchemy.ext.serializer import loads, dumps

from repository.UserRepository import *
from setting import async_session

compilers = {
    "c": "gcc 12.1.0",
    "charp": "mcs 6.12.0.122",
    "cpp": "gcc 12.1.0",
    "go": "go 1.16.3",
    "java": "OpenJDK jdk-15.0.3+2",
    "javascript": "Node.js 16.14.0",
    "php": "php 8.0.3",
    "perl": "perl 5.34.0",
    "python": "CPython 3.8.9",
    "r": "R 4.0.5",
    "ruby": "ruby 3.1.0",
    "rust": "rust 1.51.0",
    "scala": "Scala 2.13.5",
    "swift": "Swift 5.3.3",
    "typescript": "TypeScript 4.2.4"
}


class ConsoleService:

    async def getConsoleResult(self):
        authorization = self.headers.get('Authorization')

        code = self.json['code']
        language = self.json['language']


        return response.json({}, headers={
            "Access-Control-Expose-Headers": "*, Authorization",
            "Authorization": authorization
        })



