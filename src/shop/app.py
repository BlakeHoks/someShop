from fastapi import FastAPI

from db import database
from .api import router

app = FastAPI()
app.include_router(router)
