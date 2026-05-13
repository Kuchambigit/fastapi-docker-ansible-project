# Import FastAPI framework
from fastapi import FastAPI

# Create FastAPI app
app = FastAPI()

# Home route
@app.get("/")
def home():
    return {"message": "FastAPI app running successfully"}
