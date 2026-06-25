from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from database.config import Base

class Ledger(Base):
    __tablename__ = "ledgers"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    group_id = Column(Integer, nullable=True) 
    name = Column(String, index=True, nullable=False)
    
    opening_balance = Column(Numeric(15, 2), default=0.00)