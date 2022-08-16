import jwt
from dotenv import load_dotenv

load_dotenv(verbose=True)

def createToken(userId):

    token = jwt.encode(userId)