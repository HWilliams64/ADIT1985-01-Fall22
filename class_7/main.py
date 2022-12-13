from typing import Union

from fastapi import FastAPI
import random

app = FastAPI()
COLORS = ('red', 'green', 'yellow', 'blue', 'orange', 'purple', 'black', 'white', 'gold', 'silver')


@app.get("/")
def read_root():
    return {"Jello": "Panda"}

@app.get("/random/number/{min_number}/{max_number}")
def random_int(min_number:int, max_number:int):
    return {"value": random.randint(min_number, max_number)}


@app.get("/random/color/")
def random_int():
    return {'color':random.choice(COLORS)}