# Import FastAPI framework
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

# Create FastAPI app
app = FastAPI()

# Enable Prometheus metrics
Instrumentator().instrument(app).expose(app)

# Home route
@app.get("/")
def home():
    return {"message": "FastAPI app running successfully"}
