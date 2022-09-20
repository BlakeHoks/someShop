from fastapi import APIRouter

from . import (
    auth,
    product,
)


router = APIRouter()
router.include_router(auth.router)
router.include_router(product.router)
