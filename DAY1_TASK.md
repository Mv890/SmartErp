#### Day 1: Requirement Analysis \& Database Design



##### 1\. Requirements Finalized

###### &#x20;We have clearly defined the MVP features—focusing on Supplier/Customer Ledgers, Item/Stock management, and Sales/Purchase Vouchers. The foundation is built on PostgreSQL to ensure complete ACID compliance, which is mandatory for a double-entry accounting system. Instead of treating "Customers" and "Suppliers" as entirely separate concepts from the accounting flow, they are tied directly to Ledgers.



##### 2\. Core Database Schema



* ##### Core Authentication \& Multi-Tenancy



|**Table Name**|**Key Columns**|**Description**|
|-|-|-|
|users|id, email, password\_hash, created\_at|Manages authentication|
|companies|id, user\_id (FK), name, gst\_number, financial\_year|Handles multi-tenancy. A user can own up to 5|



###### 

* ##### The Masters Module (Accounting \& Inventory)

##### This is the static data that your vouchers will reference.

##### 

|**Table**|**NameKey**|**ColumnsDescription**|
|-|-|-|
|groups|id, company\_id (FK), name, nature|Categorizes ledgers for financial reports|
|ledger|id, company\_id (FK), group\_id (FK), name, opening\_balance|Represents entities like Cash, Bank, Supplier A, or Sales Account|
|unit|id, company\_id (FK), symbol, formal\_name|Defines how stock is measured|
|stock\_items|id, company\_id (FK), name, sku, unit\_id (FK), purchase\_price, selling\_price, gst\_percentage|The master list of inventory items|



* ##### The Transactional Core (Double-Entry System)



|**Table Name**|**Key Columns**|**Description**|
|-|-|-|
|vouchers|id, company\_id (FK), type, date, ref\_number, total\_amount|The header for any transaction|
|voucher\_entries|id, voucher\_id (FK), ledger\_id (FK), debit\_amount, credit\_amount|The double-entry log. Every voucher must have entries where Total Debits = Total Credits|
|inventory\_transactions|id, voucher\_id (FK), stock\_item\_id (FK), quantity, rate, amount, type|Tracks stock movement tied to specific vouchers|



##### 3\. Critical Implementation Rules



* ###### Strict Typing for Currency:Standard Python floats and JavaScript numbers are dangerous for accounting due to precision issues. For all amount, purchase\_price, selling\_price, and balance columns, you must use PostgreSQL's DECIMAL(15, 2) or NUMERIC(15, 2) types.



* ###### Data Integrity: Ensure ON DELETE CASCADE is set carefully. If a user tries to delete a ledger that has existing voucher\_entries, the database must restrict that deletion to preserve historical data integrity.



