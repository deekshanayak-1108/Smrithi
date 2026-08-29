from fastapi import FastAPI

from app.routes import (
    profile,
    sessions,
    settings,
    voice,
)


app = FastAPI(
    title="Sparsh API"
)


# ---------------------------------------------------------
# Existing Routes
# ---------------------------------------------------------

app.include_router(profile.router)
app.include_router(sessions.router)
app.include_router(settings.router)


# ---------------------------------------------------------
# Voice Layer
# ---------------------------------------------------------

app.include_router(voice.router)


# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------

@app.get("/")
def health_check():
    return {
        "status": "ok"
    }