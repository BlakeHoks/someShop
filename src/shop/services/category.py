from typing import Optional, List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db.database import get_session
from .. import models, db


class CategoryService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_by_id(self, category_id: int) -> db.Category:
        category = self._get(category_id)
        return category

    def get_all(self) -> List[db.Category]:
        categories = (
            self.session
            .query(db.Category)
            .all()
        )
        return categories

    def create(self, category_data: models.CategoryCreate) -> db.Category:
        category = db.Category(
            **category_data.dict()
        )
        self.session.add(category)
        self.session.commit()
        return category

    def update(self, category_id: int, category_data: models.CategoryUpdate) -> db.Category:
        category = self._get(category_id)
        for field, value in category_data:
            setattr(category, field, value)
        self.session.commit()
        return category

    def delete(self, category_id: int):
        category = self._get(category_id)
        self.session.delete(category)
        self.session.commit()

    def _get(self, category_id: int) -> Optional[db.Category]:
        category = (
            self.session
            .query(db.Category)
            .filter(
                db.Category.id == category_id
            )
            .first()
        )
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Non-existent id'
            )
        return category
