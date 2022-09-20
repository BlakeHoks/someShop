from pydantic import BaseModel, AnyUrl
from ..db.order import OrderStatus


class BaseOrder(BaseModel):
    user_id: int
    sum: float
    status: OrderStatus


class OrderCreate(BaseOrder):
    pass


class OrderUpdate(BaseOrder):
    pass


class Order(BaseOrder):
    id: int

    class Config:
        orm_mode = True
