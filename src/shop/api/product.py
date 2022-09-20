from typing import List

from fastapi import APIRouter, Depends, status, Response

from ..models.product import (
    Product,
    ProductCreate,
    ProductUpdate,
)
from ..services.product import ProductService


router = APIRouter(
    prefix="/products",
)


@router.get('/{product_id}', response_model=Product)
def get_product(product_id: int, product_service: ProductService = Depends()):
    return product_service.get_by_id(product_id)


@router.get('/{author}', response_model=List[Product])
def get_category(author: str, product_service: ProductService = Depends()):
    return product_service.get_by_author(author)


@router.get('/{category_id}', response_model=List[Product])
def get_category(category_id: int, product_service: ProductService = Depends()):
    return product_service.get_by_category(category_id)


@router.post('/', response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(product_data: ProductCreate, product_service: ProductService = Depends()):
    return product_service.create(product_data)


@router.put('/{product_id}', response_model=Product)
def update_product(product_id: int, product_data: ProductUpdate, product_service: ProductService = Depends()):
    return product_service.update(product_id, product_data)


@router.delete('/{product_id}', response_model=Product, status_code=status.HTTP_204_NO_CONTENT)
def update_product(product_id: int, product_service: ProductService = Depends()):
    product_service.delete(product_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
