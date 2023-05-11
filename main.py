import os

from fastapi import FastAPI, UploadFile, File
import uvicorn
from dotenv import load_dotenv
from fastapi.responses import RedirectResponse
import shutil

load_dotenv()
path = 'maedia'

app = FastAPI(
    title="FAST API",
    description="",
    version="0.0.1",
    contact={
        "name": "Kravets Olexandr",
        "email": "krava198383@gmail.com",
    },

)

'''start page redirect to docs swagger'''


@app.get("/", response_class=RedirectResponse)
async def docs():
    # return {"message": "Hello World"} '''start page'''
    return '/docs/'


@app.get("/users/")
async def get_users():
    return [{"name": "Harry"}, {"name": "Ron"}]


@app.post("/main/")
async def main(file: UploadFile = File(...)):
    with open(f"{path}\{file.filename}", "wb") as temp_data:
        shutil.copyfileobj(file.file, temp_data)
    return {"file_name": file.filename}


bb = 33

if __name__ == "__main__":
    uvicorn.run('main:app', host=str(os.getenv('HOST')), port=int(os.getenv('PORT')), reload=True)
