from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/dashboard", tags=["Dashboard Aggregation"])

@router.get("/summary/{company_id}")
def get_dashboard_summary(company_id: int):
  
    
    return {
        "company_id": company_id,
        "metrics": {
            "total_sales_mtd": 150000.00,
            "total_purchases_mtd": 85000.00,
            "cash_in_hand": 25000.00,
            "bank_balance": 340000.00
        },
        "recent_transactions": [
            {"date": "2023-10-25", "type": "Sales", "amount": 12500.00},
            {"date": "2023-10-24", "type": "Payment", "amount": 5000.00}
        ]
    }