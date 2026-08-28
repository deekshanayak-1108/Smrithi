from pydantic import BaseModel

class ReminderCreate(BaseModel):
    patient_id: str
    type: str        # "medicine" | "hydration" | "activity"
    time: str         # "HH:MM"

class ReminderStatus(BaseModel):
    reminder_id: str
    completed: bool