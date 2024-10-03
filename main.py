from fastapi import FastAPI, UploadFile, File

from fastapi.responses import FileResponse
from my_utils.utils import start_llm
import uvicorn


app = FastAPI()


@app.get("/")
async def read_root():
    return {'12': 34}


@app.get("/text-by-url")
async def text_by_url(url: str):
    text = await start_llm(url)
    return {'text': text}


@app.get("/file/download")
async def download_file():
    return FileResponse(path='data.txt', filename='data.txt', media_type='multipart/form-data')


@app.post("/file/upload-bytes")
async def upload_file_bytes(file_bytes: bytes = File()):
    return {'file_bytes': str(file_bytes)}


@app.post("/file/upload-file")
async def upload_file(file: UploadFile):
    return file


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
