from sanic import Sanic
from sanic import response
import requests
import time
from models.User import User
from .clientJwt import *
from repository.TestCaseRepository import *
from models.Testcase import *
import json
from sqlalchemy.ext.serializer import loads, dumps

from repository.UserRepository import *
from setting import async_session

compilers = {
    "c": "gcc-12.1.0",
    "charp": "mcs-6.12.0.122",
    "cpp": "gcc-12.1.0",
    "go": "go-1.16.3",
    "java": "openjdk-jdk-15.0.3+2",
    "javascript": "node.js-16.14.0",
    "php": "php-8.0.3",
    "perl": "perl-5.34.0",
    "python": "cpython-3.8.9",
    "r": "r-4.0.5",
    "ruby": "ruby-3.1.0",
    "rust": "rust-1.51.0",
    "scala": "scala-2.13.5",
    "swift": "swift-5.3.3",
    "typescript": "typeScript-4.2.4"
}


class ConsoleService:

    async def getConsoleResult(self):
        authorization = self.headers.get('Authorization')

        code = """
def is_prime(n):
    if n < 2:
        return False
    for k in range(2, int(n/2)+1):
        if n % k == 0:
            return False
    return True
print(is_prime(5))
        """

        verifyTokenResult = verifyToken(authorization)

        if verifyTokenResult['status'] != 200:
            return response.json(verifyTokenResult, status=400)


        code = self.json['code']
        language = self.json['language']

        testCaseModel = await TestCaseRepository.getTestCase(self.json['questionId'])

        res = requests.post("https://wandbox.org/api/compile.json",
                                 json={"code": code, "compiler": compilers[language], "stdin": testCaseModel.testcasesInput},
                                 headers={"Content-type": "application/json"})

        resDict= res.json()

        isError = True if resDict["status"] != '0' else False


        return response.json({
            "status": 200,
            "isError": isError,
            "programError": resDict["program_error"],
            "programOutput": resDict["program_output"]
        }, headers={
            "Access-Control-Expose-Headers": "*, Authorization",
            "Authorization": authorization
        })

    async def getTestCaseResult(self):

        authorization = self.headers.get('Authorization')

        code = """
inputNum = input()
for i in range(int(inputNum)+1):
    if i % 2 == 0:
        print(i, end=' ')
                """

        verifyTokenResult = verifyToken(authorization)

        if verifyTokenResult['status'] != 200:
            return response.json(verifyTokenResult, status=400)

        questionId = self.json["testId"]
        code = self.json["code"]
        compiler = compilers[self.json["language"]]

        testCasesModel = await TestCaseRepository.getTestCases(questionId)

        result = []
        testCaseTotal = len(testCasesModel)
        testCaseClearTotal = 0

        for testCaseModel in testCasesModel:
            res = requests.post("https://wandbox.org/api/compile.json",
                                json={"code": code, "compiler": compiler, "stdin": testCaseModel.testcasesInput},
                                headers={"Content-type": "application/json"})
            resJson = res.json()

            print(resJson)

            isClearTestCase = False
            isCompileError = False
            compilerError = ""

            if resJson["status"] == "0":
                if resJson["program_output"].strip() == testCaseModel.testcasesOutput:
                    testCaseClearTotal += 1
                    isClearTestCase = True
                    print("成功")
            else:
                isCompileError = True
                compilerError = resJson["program_error"]

            result.append({
                "testCaseId": testCaseModel.id,
                "isCompileError": isCompileError,
                "compilerError": compilerError,
                "isClearTestCase": isClearTestCase
            })
            time.sleep(0.3)

        isClearTestCases = True if testCaseClearTotal == testCaseTotal else False

        return response.json({
            "status": 200,
            "questionId": questionId,
            "isClearTestCases": isClearTestCases,
            "testCaseTotal": testCaseTotal,
            "testCaseClearTotal": testCaseClearTotal,
            "testCases": result
        }, headers={
            "Access-Control-Expose-Headers": "*, Authorization",
            "Authorization": authorization
        })
