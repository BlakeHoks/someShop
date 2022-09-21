from fastapi import FastAPI

from .api import router

app = FastAPI(
    title='BookShop',
    description='Книжный интернет-магазин',
)

app.include_router(router)
