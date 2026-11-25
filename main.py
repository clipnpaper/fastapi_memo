# main.py 저장 

from fastapi import FastAPI     #FastAPI 라이브러리를 import 합니다.

app = FastAPI()   # FastAPI 인스턴스를 생성

@app.get('/')   # HTTP GET 요청을 "/" 경로로 받을 준비 
async def read_root():
    return {"message": "Hello, World!"}  # FastAPI가 자동으로 JSON 형식으로 응답을 반환 

@app.get("/about")
async def about():
    return {"message": "이것은 마이 메모 앱의 소개 페이지입니다."}