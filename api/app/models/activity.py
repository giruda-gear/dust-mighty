import datetime
from decimal import Decimal
from typing import Optional
import uuid
from sqlalchemy import Date, DateTime, ForeignKey, Integer, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base, TimestampMixin


class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    unit_count: Mapped[int] = mapped_column(Integer)
    earned_points: Mapped[int] = mapped_column(Integer)
    note: Mapped[Optional[str]] = mapped_column(String(200))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    logged_date: Mapped[datetime.date] = mapped_column(Date)
