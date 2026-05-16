from fastapi import FastAPI, Request
from app.api.users import router as users_router
from app.api.health import router as health_router

app = FastAPI(title="FastAPI Backend System Design")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request received: {request.url}")
    response = await call_next(request)
    return response


app.include_router(users_router)
app.include_router(health_router)


@app.get("/")
async def root():
    return {"message": "Backend running successfully"}