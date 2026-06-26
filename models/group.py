from sqlalchemy import Column, Integer, String, ForeignKey
from database.config import Base

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    name = Column(String, index=True, nullable=False)
    nature = Column(String, nullable=False) 