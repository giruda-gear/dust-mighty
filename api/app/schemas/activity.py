from datetime import date
from pydantic import BaseModel, field_validator


class ActivityCreate(BaseModel):
    category_id: int
    unit_count: int
    note: str | None = None
    logged_date: date

    @field_validator("logged_date")
    @classmethod
    def not_future(cls, v: date) -> date:
        if v > date.today():
            raise ValueError("logged_date cannot be in the future")
        return v

class ActivityResponse(BaseModel):
    unit_count: str
    earned_points: int
    note: str
