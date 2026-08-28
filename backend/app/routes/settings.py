from fastapi import APIRouter
from app.models.patient import PatientSettings
from app.services.firestore_service import update_settings

router = APIRouter(prefix="/settings", tags=["settings"])

@router.put("/{patient_id}")
def set_settings(patient_id: str, settings: PatientSettings):
    update_settings(patient_id, settings.model_dump())
    return {"status": "updated"}