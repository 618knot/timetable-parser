from newJSON import newJSON
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def outputJSON():
    return newJSON()