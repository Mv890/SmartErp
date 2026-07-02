from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import all the route modules
from routes import auth, company, dashboard, ledger, group, inventory, voucher, billing, reports, search

app = FastAPI(title="SmartERP API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(company.router)
app.include_router(dashboard.router)
app.include_router(ledger.router)
app.include_router(group.router)
app.include_router(inventory.router)
app.include_router(voucher.router)
app.include_router(billing.router)
app.include_router(reports.router)
app.include_router(search.router) 

@app.get("/")
def health_check():
    return {"status": "System Online", "module": "SmartERP Core Gateway"}