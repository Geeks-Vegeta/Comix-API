from typing import Union
from fastapi import Depends, FastAPI, HTTPException, status
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from routes import nhentai_route, xhamster_route,\
    eightmuses_route, porncomics_route, kingcomics_route


description = '''

This is an example of blog api
For NextJs Blogging Application
💋

'''

app = FastAPI(
    title="Blog API",
    description=description,
    version=0.1
)


origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Ok"}

app.include_router(nhentai_route.route)
app.include_router(xhamster_route.route)
app.include_router(eightmuses_route.route)
app.include_router(porncomics_route.route)
app.include_router(kingcomics_route.route)


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, port=3000)