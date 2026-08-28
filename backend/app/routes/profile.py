from fastapi import APIRouter, HTTPException
from app.models.patient import PatientProfile
from app.services.firestore_service import create_patient, get_patient

router = APIRouter(prefix="/profile", tags=["profile"])

@router.post("/")
def create_profile(profile: PatientProfile):
    patient_id = create_patient(profile.model_dump())
    return {"patient_id": patient_id}

@router.get("/{patient_id}")
def read_profile(patient_id: str):
    patient = get_patient(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient