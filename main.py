from fastapi import FastAPI
from utils import generate_passphrase

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/gen_pass/{lengh}")
async def gen_passphase(lengh: int):
    return {"passphase": generate_passphrase(lengh)}
