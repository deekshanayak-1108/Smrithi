from app.core.firebase_init import db
from datetime import datetime

def _get_db():
    if db is None:
        raise RuntimeError("Firestore client is not initialized. Please ensure 'serviceAccountKey.json' contains valid Firebase service account credentials.")
    return db

def create_patient(patient_data: dict) -> str:
    doc_ref = _get_db().collection("patients").document()
    doc_ref.set(patient_data)
    return doc_ref.id

def get_patient(patient_id: str) -> dict:
    doc = _get_db().collection("patients").document(patient_id).get()
    return doc.to_dict() if doc.exists else None

def add_session(patient_id: str, session_data: dict) -> str:
    session_data["timestamp"] = datetime.utcnow()
    doc_ref = _get_db().collection("patients").document(patient_id).collection("sessions").document()
    doc_ref.set(session_data)
    return doc_ref.id

def get_sessions(patient_id: str) -> list:
    docs = _get_db().collection("patients").document(patient_id).collection("sessions").stream()
    return [{**doc.to_dict(), "session_id": doc.id} for doc in docs]

def update_settings(patient_id: str, settings: dict):
    _get_db().collection("patients").document(patient_id).collection("settings").document("config").set(settings, merge=True)