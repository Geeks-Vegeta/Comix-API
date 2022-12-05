from fastapi import APIRouter, status
from typing import List, Union
from functions.comics import porncomics_download

route = APIRouter(
    tags=["porncomics"],
)


@route.post("/porncomics",responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "Return the pdf of comics.",
        }
    }, include_in_schema=False)
async def porncomics(url:str):
    return porncomics_download(url)