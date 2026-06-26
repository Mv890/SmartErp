from pydantic import BaseModel

class GroupCreate(BaseModel):
    name: str
    nature: str

class GroupResponse(GroupCreate):
    id: int
    company_id: int

    class Config:
        from_attributes = True