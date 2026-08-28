from pydantic import BaseModel
from datetime import datetime

class SessionCreate(BaseModel):
    patient_id: str
    game_type: str          # "memory_recall" | "pattern_recognition"
    accuracy: float          # 0-100
    response_time_avg: float # seconds
    difficulty_level: str

class SessionResponse(SessionCreate):
    session_id: str
    timestamp: datetime