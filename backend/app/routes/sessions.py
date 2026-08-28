from fastapi import APIRouter
from app.models.session import SessionCreate
from app.services.firestore_service import add_session, get_sessions

router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.post("/")
def submit_session(session: SessionCreate):
    session_id = add_session(session.patient_id, session.model_dump())
    return {"session_id": session_id}

@router.get("/{patient_id}")
def list_sessions(patient_id: str):
    return get_sessions(patient_id)