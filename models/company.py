from sqlalchemy import Column, Integer, String, ForeignKey
from database.config import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, index=True, nullable=False)
    gst_number = Column(String)
    financial_year = Column(String, nullable=False)