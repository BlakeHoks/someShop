from typing import Optional, List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db.database import get_session
from .. import models, db


class ProductService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_by_id(self, product_id: int) -> db.Product:
        product = self._get(product_id)
        return product

    def get_by_category(self, category_id: int) -> List[db.Product]:
        products = (
            self.session
            .query(db.Product)
            .filter(db.Product.category_id == category_id)
            .order_by(db.Product.id)
            .all()
        )
        return products

    def create(self, product_data: models.ProductCreate) -> db.Product:
        product = db.Product(
            **product_data.dict()
        )
        self.session.add(product)
        self.session.commit()
        return product

    def update(self, product_id: int, product_data: models.ProductUpdate) -> db.Product:
        product = self._get(product_id)
        for field, value in product_data:
            setattr(product, field, value)
        self.session.commit()
        return product

    def delete(self, product_id: int):
        product = self._get(product_id)
        self.session.delete(product)
        self.session.commit()

    def _get(self, product_id: int) -> Optional[db.Product]:
        product = (
            self.session
            .query(db.Product)
            .filter(
                db.Product.id == product_id
            )
            .first()
        )
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Non-existent id'
            )
        return product
