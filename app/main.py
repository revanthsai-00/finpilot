
from fastapi import FastAPI

app = FastAPI(
    title="FinPilot API",
    description="An AI-powered personal finance SaaS platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "app": "FinPilot",
        "message": "Your financial co-pilot is running!",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "finpilot-api",
    }
