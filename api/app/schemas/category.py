from decimal import Decimal
from pydantic import BaseModel


class CategoryResponse(BaseModel):
    id: int
    name: str
    points_per_unit: int
    color: str | None
    icon: str | None

    model_config = {"from_attributes": True}
