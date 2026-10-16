
from fastapi import FastAPI

app = FastAPI(
    title="CloudSecOps Demo API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "CloudSecOps AI",
        "message": "DevSecOps platform is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
