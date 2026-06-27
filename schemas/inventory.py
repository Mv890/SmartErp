from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Optional

class UnitCreate(BaseModel):
    symbol: str
    formal_name: Optional[str] = None

class UnitResponse(UnitCreate):
    id: int
    company_id: int

    class Config:
        from_attributes = True
        
class StockItemCreate(BaseModel):
    name: str
    sku: Optional[str] = None
    unit_id: int
    purchase_price: Decimal = Field(default=Decimal('0.00'), max_digits=15, decimal_places=2)
    selling_price: Decimal = Field(default=Decimal('0.00'), max_digits=15, decimal_places=2)
    gst_percentage: Decimal = Field(default=Decimal('0.00'), max_digits=5, decimal_places=2)

class StockItemResponse(StockItemCreate):
    id: int
    company_id: int

    class Config:
        from_attributes = True