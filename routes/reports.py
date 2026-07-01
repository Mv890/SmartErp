from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict

router = APIRouter(prefix="/reports", tags=["Reports Module"])

@router.get("/financial/balance-sheet/{company_id}")
def get_balance_sheet(company_id: int):
   
    return {
        "company_id": company_id,
        "report_type": "Balance Sheet",
        "assets": {
            "current_assets": 450000.00,
            "fixed_assets": 1200000.00,
            "total": 1650000.00
        },
        "liabilities": {
            "current_liabilities": 150000.00,
            "long_term_liabilities": 500000.00,
            "capital_account": 1000000.00,
            "total": 1650000.00
        }
    }

@router.get("/inventory/stock-summary/{company_id}")
def get_stock_summary(company_id: int):
  
    return {
        "company_id": company_id,
        "report_type": "Stock Summary",
        "items": [
            {"item_name": "Wireless Mouse", "closing_quantity": 45, "value": 22500.00},
            {"item_name": "Mechanical Keyboard", "closing_quantity": 12, "value": 42000.00}
        ],
        "total_inventory_value": 64500.00
    }