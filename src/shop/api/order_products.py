from typing import List

from fastapi import APIRouter, Depends, status, Response

from ..models.order_products import (
    OrderProducts,
    OrderProductsCreate,
    OrderProductsUpdate,
)
from ..services.order_products import OrderProductsService


router = APIRouter(
    prefix="/cart",
)
# TODO: скорее всего здесь что-то придётся исправлять


@router.get('/{order_id}', response_model=OrderProducts)
def get_order_products(order_id: int, order_products_service: OrderProductsService = Depends()):
    return order_products_service.get(order_id)


@router.post('/', response_model=OrderProducts, status_code=status.HTTP_201_CREATED)
def create_product(order_products_data: OrderProductsCreate, order_service: OrderProductsService = Depends()):
    return order_service.create(order_products_data)


@router.put('/{order_id, product_id}', response_model=OrderProducts)
def update_product(order_id: int, product_id: int, order_products_data: OrderProductsUpdate, order_service: OrderProductsService = Depends()):
    return order_service.update(order_id, product_id, order_products_data)


@router.delete('/{order_id, product_id}', response_model=OrderProducts, status_code=status.HTTP_204_NO_CONTENT)
def update_product(order_id: int, product_id: int, order_service: OrderProductsService = Depends()):
    order_service.delete(order_id, product_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
