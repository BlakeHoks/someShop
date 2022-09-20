from pydantic import BaseModel, AnyUrl


class BaseProduct(BaseModel):
    name: str
    author: str
    description: str
    image: AnyUrl
    price: int
    category_id: int


class ProductCreate(BaseProduct):
    pass


class ProductUpdate(BaseProduct):
    pass


class Product(BaseProduct):
    id: int

    class Config:
        orm_mode = True
