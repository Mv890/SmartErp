from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/search", tags=["Global Search"])

@router.get("/")
def global_search(query: str):
  
    return {
        "query": query,
        "results": {
            "ledgers": [{"id": 1, "name": "Acme Corp", "type": "Customer"}],
            "vouchers": [{"id": 102, "type": "Sales", "amount": 15000.00}],
            "inventory": [{"id": 5, "name": "Wireless Mouse", "stock": 45}]
        }
    }