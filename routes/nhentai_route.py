from fastapi import APIRouter, status
from typing import List, Union
from functions.comics import nhentai_download

route = APIRouter(
    tags=["nHentai"],
)


@route.post("/nhentai_io",responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "Return the pdf of comics.",
        }
    })
async def nhentai_io(url:str):
    # https://nhentai.xxx/g/412151/
    return nhentai_download(url)