from mosaicGenerator import generateMosaic
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
async def createMosaic(file: UploadFile = File(...), sampleSize: int = 25):
    with open("test.png", "wb+") as file_object:
        file_object.write(file.file.read())
    output = generateMosaic("test.png", sampleSize)
    return {"output": output}