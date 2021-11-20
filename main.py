from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from energy_calculator import best_server_location

app = FastAPI()


class Body(BaseModel):
    countries: List[str]
    nuclear_is_green = False


@app.post("/ranking")
async def root(body: Body):
    return best_server_location(body.countries, nuclear_is_green=body.nuclear_is_green)
