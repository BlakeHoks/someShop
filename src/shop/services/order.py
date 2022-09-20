from typing import Optional, List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db.database import get_session
from .. import models, db


class OrderService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_by_id(self, order_id: int) -> db.Order:
        order = self._get(order_id)
        return order

    def get_by_user_id(self, user_id: int) -> List[db.Order]:
        orders = (
            self.session
            .query(db.Order)
            .filter(db.Order.user_id == user_id)
            .all()
        )
        return orders

    def create(self, order_data: models.OrderCreate) -> db.Order:
        order = db.Order(
            **order_data.dict()
        )
        self.session.add(order)
        self.session.commit()
        return order

    def update(self, order_id: int, order_data: models.OrderUpdate) -> db.Order:
        order = self._get(order_id)
        for field, value in order_data:
            setattr(order, field, value)
        self.session.commit()
        return order

    def delete(self, order_id: int):
        order = self._get(order_id)
        self.session.delete(order)
        self.session.commit()

    def _get(self, order_id: int) -> Optional[db.Order]:
        order = (
            self.session
            .query(db.Order)
            .filter(
                db.Order.id == order_id
            )
            .first()
        )
        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Non-existent id'
            )
        return order
