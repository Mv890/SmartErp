from fastapi import APIRouter, Depends, HTTPException, status
from schemas.group import GroupCreate, GroupResponse

router = APIRouter(prefix="/groups", tags=["Group Management"])

@router.post("/", response_model=GroupResponse)
def create_group(group: GroupCreate):
    
    return {
        "id": 1,
        "company_id": 1, # Mocked active company ID
        "name": group.name,
        "nature": group.nature
    }