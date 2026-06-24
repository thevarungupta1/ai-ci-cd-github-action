from fastapi import FastAPI
from app.health import get_health_status

app = FastAPI(
    title = "AI CI/CD Service",
    version = "1.0.0",
)

@app.get("/health")
def health():
    return get_health_status()