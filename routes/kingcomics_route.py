from fastapi import APIRouter, status
from typing import List, Union
from functions.comics import king_download

route = APIRouter(
    tags=["kingcomics"],
)


@route.post("/kingcomics",responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "Return the pdf of comics.",
        }
    })
async def kingcomics(url:str):
    return king_download(url)