# Import FastAPI framework
from fastapi import FastAPI

# Create FastAPI application
app = FastAPI()

# Home route
@app.get("/")
def home():

    # Return JSON response
    return {
        "message": "Hello from FastAPI with Docker and Ansible!"
    }
