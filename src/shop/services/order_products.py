from typing import Optional, List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db.database import get_session
from .. import models, db


class OrderProductsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_by_id(self, order_id: int) -> db.Order:
        order = self._get(order_id)
        return order

    def create(self, order_id: int, order_product_data: models.OrderProductsCreate) -> db.OrderProducts:
        order_products = db.OrderProducts(
            **order_product_data.dict(),
            order_id=order_id
        )
        self.session.add(order_products)
        self.session.commit()
        return order_products

    def update(self, order_id: int, product_id: int, order_product_data: models.OrderProductsUpdate) -> db.OrderProducts:
        order_products = self._get(order_id, product_id)
        for field, value in order_product_data:
            setattr(order_products, field, value)
        self.session.commit()
        return order_products

    def delete(self, order_id: int, product_id: int):
        order_products = self._get(order_id, product_id)
        self.session.delete(order_products)
        self.session.commit()

    def _get(self, order_id: int, product_id: int) -> Optional[db.OrderProducts]:
        order_products = (
            self.session
            .query(db.OrderProducts)
            .filter(
                db.OrderProducts.order_id == order_id,
                db.OrderProducts.product_id == product_id
            )
            .first()
        )
        if not order_products:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Non-existent id'
            )
        return order_products
