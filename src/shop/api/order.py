from typing import List

from fastapi import APIRouter, Depends, status, Response

from ..models.order import (
    Order,
    OrderCreate,
    OrderUpdate,
)
from ..services.order import OrderService


router = APIRouter(
    prefix="/orders",
)


@router.get('/{order_id}', response_model=Order)
def get_order(order_id: int, order_service: OrderService = Depends()):
    return order_service.get_by_id(order_id)


@router.get('/{user_id}', response_model=List[Order])
def get_order(user_id: int, order_service: OrderService = Depends()):
    return order_service.get_by_user_id(user_id)


@router.post('/', response_model=Order, status_code=status.HTTP_201_CREATED)
def create_product(order_data: OrderCreate, order_service: OrderService = Depends()):
    return order_service.create(order_data)


@router.put('/{order_id}', response_model=Order)
def update_product(order_id: int, order_data: OrderUpdate, order_service: OrderService = Depends()):
    return order_service.update(order_id, order_data)


@router.delete('/{order_id}', response_model=Order, status_code=status.HTTP_204_NO_CONTENT)
def update_product(order_id: int, order_service: OrderService = Depends()):
    order_service.delete(order_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
