from decimal import Decimal
from tokenize import String
from typing import Optional
import uuid
from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base, TimestampMixin


class Activity(TimestampMixin, Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    unit_count: Mapped[Decimal] = mapped_column(Numeric(6, 1))
    earned_points: Mapped[Decimal] = mapped_column(Numeric(6, 1))
    note: Mapped[Optional[str]] = mapped_column(String(200))