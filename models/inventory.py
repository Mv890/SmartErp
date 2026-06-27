from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from database.config import Base

class Unit(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    symbol = Column(String, index=True, nullable=False) 
    formal_name = Column(String) 
    
class StockItem(Base):
    __tablename__ = "stock_items"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    name = Column(String, index=True, nullable=False)
    sku = Column(String, unique=True, index=True)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=False)
    
    # Financials and Taxes
    purchase_price = Column(Numeric(15, 2), default=0.00)
    selling_price = Column(Numeric(15, 2), default=0.00)
    gst_percentage = Column(Numeric(5, 2), default=0.00)