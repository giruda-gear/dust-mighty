from datetime import date
from decimal import Decimal
from pydantic import BaseModel


class ActivityCreate(BaseModel):
    category_id: int
    unit_count: int
    note: str | None = None
    logged_date: date


class ActivityResponse(BaseModel):
    unit_count: str
    earned_points: int
    note: str
