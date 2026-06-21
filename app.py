from fastapi import FastAPI

app = FastAPI(title="SmartERP API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the SmartERP Backend!"}