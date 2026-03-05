from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "service": os.getenv("SERVICE_NAME", "microservice"),
        "env": os.getenv("ENV", "dev"),
        "message": "OK Todo funcionando de forma correcta."
    }