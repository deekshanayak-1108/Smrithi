from fastapi import FastAPI
from app.routes import profile, sessions, settings

app = FastAPI(title="Sparsh API")

app.include_router(profile.router)
app.include_router(sessions.router)
app.include_router(settings.router)

@app.get("/")
def health_check():
    return {"status": "ok"}