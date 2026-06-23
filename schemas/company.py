from pydantic import BaseModel
from typing import Optional

class CompanyCreate(BaseModel):
    name: str
    gst_number: Optional[str] = None
    financial_year: str

class CompanyResponse(CompanyCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True