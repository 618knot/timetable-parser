from app.newJSON import newJSON
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def outputJSON():
    return newJSON()