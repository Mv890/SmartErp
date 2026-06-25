from fastapi import APIRouter, Depends, HTTPException, status
from schemas.ledger import LedgerCreate, LedgerResponse

router = APIRouter(prefix="/ledgers", tags=["Master Ledgers"])

@router.post("/", response_model=LedgerResponse)
def create_ledger(ledger: LedgerCreate):
    
    return {
        "id": 1,
        "company_id": 1, # Mocked active company ID
        "name": ledger.name,
        "group_id": ledger.group_id,
        "opening_balance": ledger.opening_balance
    }