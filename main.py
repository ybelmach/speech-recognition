from fastapi import FastAPI, UploadFile, File

from fastapi.responses import FileResponse
import uvicorn
from requests import Request

app = FastAPI()


@app.get("/")
def read_root():
    return {'12': 34}


@app.get("/file/download")
def download_file():
    return FileResponse(path='data.txt', filename='data.txt', media_type='multipart/form-data')


@app.post("/file/upload-bytes")
def upload_file_bytes(file_bytes: bytes = File()):
    return {'file_bytes': str(file_bytes)}


@app.post("/file/upload-file")
def upload_file(file: UploadFile):
    return file


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
