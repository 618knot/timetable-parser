from fastapi import FastAPI
import sys
import app.pdfManager as pdfManager
import app.jsonManager as jsonManager

app = FastAPI()
pdfM = pdfManager.PdfManager()
jsonM = jsonManager.JsonManager()

@app.get("/")
async def get_json():
    return jsonM.new_json()

@app.get("/getpdf")
def get_pdf():
    pdfM.get_pdf_from_web()