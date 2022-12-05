from fastapi import HTTPException, status
from fastapi.responses import JSONResponse, RedirectResponse
import os
from dotenv import load_dotenv 
from datetime import datetime, timedelta
from bson.objectid import ObjectId


load_dotenv()