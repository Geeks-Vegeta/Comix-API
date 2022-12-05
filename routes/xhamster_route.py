from fastapi import APIRouter, status
from typing import List, Union
from functions.comics import xhamster_download

route = APIRouter(
    tags=["xhamster"],
)


@route.get("/xhamster",responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "Return the pdf of comics.",
        }
    })
async def xhamster_desi(url:str):
    return xhamster_download(url)