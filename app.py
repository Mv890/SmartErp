from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import all the route modules
from routes import auth, company, dashboard, ledger, group

app = FastAPI(title="SmartERP API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register the routers
app.include_router(auth.router)
app.include_router(company.router)
app.include_router(dashboard.router)
app.include_router(ledger.router)
app.include_router(group.router) # <-- Newly added for Day 7

@app.get("/")
def health_check():
    return {"status": "System Online", "module": "SmartERP Core Gateway"}