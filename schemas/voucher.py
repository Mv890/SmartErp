from pydantic import BaseModel, Field
from decimal import Decimal
from typing import List, Optional
from datetime import date

class VoucherEntryCreate(BaseModel):
    ledger_id: int
    debit_amount: Decimal = Field(default=Decimal('0.00'), max_digits=15, decimal_places=2)
    credit_amount: Decimal = Field(default=Decimal('0.00'), max_digits=15, decimal_places=2)

class InventoryTransactionCreate(BaseModel):
    stock_item_id: int
    quantity: Decimal
    rate: Decimal
    amount: Decimal
    type: str


class VoucherCreate(BaseModel):
    type: str
    date: date
    ref_number: Optional[str] = None
    total_amount: Decimal = Field(..., max_digits=15, decimal_places=2)
 
    entries: List[VoucherEntryCreate]
    inventory: Optional[List[InventoryTransactionCreate]] = []

class VoucherResponse(BaseModel):
    id: int
    company_id: int
    status: str = "Voucher Successfully Posted"

    class Config:
        from_attributes = True