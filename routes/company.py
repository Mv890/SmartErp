from fastapi import APIRouter, Depends, HTTPException, status
from schemas.company import CompanyCreate, CompanyResponse

router = APIRouter(prefix="/companies", tags=["Company Management"])

@router.post("/", response_model=CompanyResponse)
def create_company(company: CompanyCreate):

    return {
        "id": 1,
        "user_id": 1, 
        "name": company.name,
        "gst_number": company.gst_number,
        "financial_year": company.financial_year
    }