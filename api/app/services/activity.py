import uuid
from typing import Annotated
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND

from app.database import get_db
from app.models.activity import Activity
from app.models.category import Category
from app.schemas.activity import ActivityCreate


class ActivityService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, activity_in: ActivityCreate, user_id: uuid.UUID) -> Activity:
        category = (
            self.db.query(Category)
            .filter(Category.id == activity_in.category_id)
            .first()
        )
        if not category:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND, detail="Category not found"
            )

        earned_points = activity_in.unit_count * category.points_per_unit

        activity = Activity(
            user_id=user_id,
            **activity_in.model_dump(),
            earned_points=earned_points,
            note=activity_in.note,
        )
        self.db.add(activity)
        self.db.commit()
        self.db.refresh(activity)
        return activity

    def get_all_by_user(self, user_id: uuid.UUID) -> list[Activity]:
        return (
            self.db.query(Activity)
            .filter(Activity.user_id == user_id)
            .order_by(Activity.logged_date.desc())
            .all()
        )


def get_activity_service(db: Session = Depends(get_db)) -> ActivityService:
    return ActivityService(db)


ActivityServiceDep = Annotated[ActivityService, Depends(get_activity_service)]
