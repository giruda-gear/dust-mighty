from decimal import Decimal
from sqlalchemy import Numeric, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base, TimestampMixin


class Category(TimestampMixin, Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    color: Mapped[str] = mapped_column(String(7), default="#000000")
    icon: Mapped[str] = mapped_column(String(30), default="default")
    points_per_unit: Mapped[Decimal] = mapped_column(Numeric(4, 1), default=Decimal("0.0"))
