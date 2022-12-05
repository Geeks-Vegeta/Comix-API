from fastapi import APIRouter, status
from typing import List, Union
from functions.comics import eightmuses_download


route = APIRouter(
    tags=["8muses"],
)


@route.post("/eightmuses",responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "Return the pdf of comics.",
        }
    })
async def eightmuses(url:str):
    return eightmuses_download(url)