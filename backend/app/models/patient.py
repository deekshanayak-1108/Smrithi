from pydantic import BaseModel
from typing import Optional

class PatientProfile(BaseModel):
    name: str
    language: str
    age: Optional[int] = None
    personalization_facts: Optional[dict] = None  # for Phase 2 LLM content

class PatientSettings(BaseModel):
    difficulty_level: str  # "easy" | "medium" | "hard"
    reminder_times: list[str] = []