from fastapi import APIRouter, HTTPException, status
from fastapi.responses import StreamingResponse
from utils.pdf_generator import generate_invoice_pdf

router = APIRouter(prefix="/billing", tags=["Billing System"])

@router.get("/invoice/{voucher_id}/pdf")
def download_invoice_pdf(voucher_id: int):
    # Future Database Logic:
    # 1. Query the 'vouchers' and 'voucher_entries' tables using voucher_id
    # 2. Extract customer details, items, and total amount
    # 3. Check if voucher type is actually 'Sales'
    
    # Mocking the database fetch for now
    mock_invoice_data = {
        "invoice_number": f"INV-2023-{voucher_id}",
        "customer_name": "Acme Corporation",
        "total_amount": "15000.00"
    }
    
    pdf_buffer = generate_invoice_pdf(mock_invoice_data)
    
    return StreamingResponse(
        pdf_buffer, 
        media_type="application/pdf", 
        headers={"Content-Disposition": f"attachment; filename=invoice_{voucher_id}.pdf"}
    )