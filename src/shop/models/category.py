from typing import Optional
from pydantic import BaseModel


class BaseCategory(BaseModel):
    name: str


class CategoryCreate(BaseCategory):
    pass


class CategoryUpdate(BaseCategory):
    pass


class Category(BaseCategory):
    id: Optional[str] = None

    class Config:
        orm_mode = True
