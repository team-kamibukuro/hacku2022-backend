import os
import datetime

import jwt

from dotenv import load_dotenv

load_dotenv(verbose=True)

algorithm="HS256"
key = os.environ.get("JWT_SECRET")

def createToken(userId, userName):

    payload = {
        "userId": userId,
        "userName": userName
    }

    dateOfExpirydatetime = str(datetime.datetime.now() + datetime.timedelta(hours=6))

    token = jwt.encode(
        headers={"exp": dateOfExpirydatetime},
        payload=payload, key=key, algorithm=algorithm)
    return token


def verifyToken(token):

    try:
        jwt.decode(token, key=key, algorithms=["HS256"])
        return {"status": 200, "message": ""}
    except jwt.ExpiredSignatureError:
        return {"status": 201, "message": "トークンの有効期限が切れています。"}
    except Exception:
        return {"status": 202, "message": "トークンの検証に失敗しました。"}



