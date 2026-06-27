from fastapi import APIRouter, Depends, HTTPException, status
from schemas.inventory import UnitCreate, UnitResponse, StockItemCreate, StockItemResponse

router = APIRouter(prefix="/inventory", tags=["Inventory Management"])

@router.post("/units", response_model=UnitResponse)
def create_unit(unit: UnitCreate):
   
    return {
        "id": 1,
        "company_id": 1, # Mocked
        "symbol": unit.symbol,
        "formal_name": unit.formal_name
    }

@router.post("/items", response_model=StockItemResponse)
def create_stock_item(item: StockItemCreate):
  
    return {
        "id": 1,
        "company_id": 1, # Mocked
        "name": item.name,
        "sku": item.sku,
        "unit_id": item.unit_id,
        "purchase_price": item.purchase_price,
        "selling_price": item.selling_price,
        "gst_percentage": item.gst_percentage
    }