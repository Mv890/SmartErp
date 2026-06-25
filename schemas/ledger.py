from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Optional

class LedgerCreate(BaseModel):
    name: str
    group_id: Optional[int] = None
    opening_balance: Decimal = Field(default=Decimal('0.00'), max_digits=15, decimal_places=2)

class LedgerResponse(LedgerCreate):
    id: int
    company_id: int

    class Config:
        from_attributes = True