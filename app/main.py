from fastapi import FastAPI


from app.api.routes import health,users,auth
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="AI-powered Job Search and Application Automation Platform",
    version="1.0.0",
)

app.include_router(health.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to JobPilot API",
        "version": "1.0.0",
    }