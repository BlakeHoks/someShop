from pydantic import BaseModel, AnyUrl


class BaseOrderProducts(BaseModel):
    order_id: int
    product_id: int
    amount: int


class OrderProductsCreate(BaseOrderProducts):
    pass


class OrderProductsUpdate(BaseOrderProducts):
    pass


class OrderProducts(BaseOrderProducts):

    class Config:
        orm_mode = True
