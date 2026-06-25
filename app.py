from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import auth, company, dashboard, ledger

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

@app.get("/")
def health_check():
    return {"status": "System Online", "module": "SmartERP Core Gateway"}