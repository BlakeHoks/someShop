from typing import List

from fastapi import APIRouter, Depends, status, Response

from ..models.category import (
    Category,
    CategoryCreate,
    CategoryUpdate,
)
from ..services.category import CategoryService


router = APIRouter(
    prefix="/categories",
)


@router.get('/{category_id}', response_model=Category)
def get_category(category_id: int, category_service: CategoryService = Depends()):
    return category_service.get_by_id(category_id)


@router.get('/', response_model=List[Category])
def get_all_categories(category_service: CategoryService = Depends()):
    return category_service.get_all()


@router.post('/', response_model=Category, status_code=status.HTTP_201_CREATED)
def create(category_data: CategoryCreate, category_service: CategoryService = Depends()):
    return category_service.create(category_data)


@router.put('/{category_id}', response_model=Category)
def update(category_id: int, category_data: CategoryUpdate, category_service: CategoryService = Depends()):
    return category_service.update(category_id, category_data)


@router.post('/{category_id}', response_model=Category, status_code=status.HTTP_204_NO_CONTENT)
def delete(category_id: int, category_service: CategoryService = Depends()):
    return category_service.delete(category_id)