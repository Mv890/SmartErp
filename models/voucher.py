from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from database.config import Base

class Voucher(Base):
    __tablename__ = "vouchers"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    type = Column(String, nullable=False) 
    date = Column(Date, nullable=False)
    ref_number = Column(String)
    total_amount = Column(Numeric(15, 2), nullable=False)

class VoucherEntry(Base):
    __tablename__ = "voucher_entries"

    id = Column(Integer, primary_key=True, index=True)
    voucher_id = Column(Integer, ForeignKey("vouchers.id", ondelete="CASCADE"), nullable=False)
    ledger_id = Column(Integer, ForeignKey("ledgers.id"), nullable=False)
    debit_amount = Column(Numeric(15, 2), default=0.00)
    credit_amount = Column(Numeric(15, 2), default=0.00)

class InventoryTransaction(Base):
    __tablename__ = "inventory_transactions"

    id = Column(Integer, primary_key=True, index=True)
    voucher_id = Column(Integer, ForeignKey("vouchers.id", ondelete="CASCADE"), nullable=False)
    stock_item_id = Column(Integer, ForeignKey("stock_items.id"), nullable=False)
    quantity = Column(Numeric(15, 2), nullable=False)
    rate = Column(Numeric(15, 2), nullable=False)
    amount = Column(Numeric(15, 2), nullable=False)
    type = Column(String, nullable=False) 