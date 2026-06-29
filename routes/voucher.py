from fastapi import APIRouter, Depends, HTTPException, status
from schemas.voucher import VoucherCreate, VoucherResponse
from decimal import Decimal

router = APIRouter(prefix="/vouchers", tags=["Transactions"])

@router.post("/purchase", response_model=VoucherResponse)
def create_purchase_voucher(voucher: VoucherCreate):
   
    total_debits = sum(entry.debit_amount for entry in voucher.entries)
    total_credits = sum(entry.credit_amount for entry in voucher.entries)
    
    if total_debits != total_credits:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Accounting Rule Violation: Total Debits must equal Total Credits."
        )

    
    return {
        "id": 1,
        "company_id": 1, # Mocked active company ID
        "status": "Purchase Voucher Successfully Posted"
    }

@router.post("/sales", response_model=VoucherResponse)
def create_sales_voucher(voucher: VoucherCreate):
    
    if voucher.type.lower() != "sales":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Invalid voucher type. Must be 'Sales'."
        )


    total_debits = sum(entry.debit_amount for entry in voucher.entries)
    total_credits = sum(entry.credit_amount for entry in voucher.entries)
    
    if total_debits != total_credits:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Accounting Rule Violation: Total Debits must equal Total Credits."
        )

    
    return {
        "id": 2, # Mocking a new ID
        "company_id": 1, # Mocked active company ID
        "status": "Sales Voucher Successfully Posted and Inventory Reduced"
    }