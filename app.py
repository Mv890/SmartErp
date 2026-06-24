from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import auth, company, dashboard

app = FastAPI(
    title="SmartERP API",
    description="Backend foundation for the Tally-inspired SmartERP platform.",
    version="1.0.0"
)

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

@app.get("/")
def health_check():
    return {"status": "System Online", "module": "SmartERP Core Gateway"}