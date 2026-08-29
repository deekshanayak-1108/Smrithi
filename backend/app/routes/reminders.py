from typing import List, Optional
from fastapi import APIRouter, HTTPException, status, Query
from app.database.db import db
from app.schemas import ReminderCreate, ReminderUpdate, ReminderResponse
from app.services.reminder_service import ReminderService

router = APIRouter(tags=["Reminders"])

@router.post("/api/reminders", response_model=ReminderResponse, status_code=status.HTTP_201_CREATED)
@router.post("/reminders", response_model=ReminderResponse, status_code=status.HTTP_201_CREATED)
def create_reminder(reminder_in: ReminderCreate):
    """Creates a new scheduled reminder for a dementia patient (medication, games, hydration, routine)."""
    patient = db.patients.find_one({"id": reminder_in.patient_id})
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID '{reminder_in.patient_id}' not found."
        )

    doc = ReminderService.create_reminder(reminder_in)
    return ReminderResponse(**doc)

@router.get("/api/reminders/patient/{patient_id}", response_model=List[ReminderResponse])
@router.get("/reminders/patient/{patient_id}", response_model=List[ReminderResponse])
def get_patient_reminders(patient_id: str, include_completed: bool = Query(True)):
    """Lists all reminders for a specific patient."""
    patient = db.patients.find_one({"id": patient_id})
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID '{patient_id}' not found."
        )

    reminders = ReminderService.get_patient_reminders(patient_id, include_completed=include_completed)
    return [ReminderResponse(**r) for r in reminders]

@router.get("/api/reminders/{reminder_id}", response_model=ReminderResponse)
def get_reminder(reminder_id: str):
    """Retrieves reminder details by reminder ID."""
    doc = ReminderService.get_reminder(reminder_id)
    if not doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Reminder with ID '{reminder_id}' not found."
        )
    return ReminderResponse(**doc)

@router.put("/api/reminders/{reminder_id}", response_model=ReminderResponse)
def update_reminder(reminder_id: str, updates_in: ReminderUpdate):
    """Updates a reminder."""
    doc = ReminderService.update_reminder(reminder_id, updates_in)
    if not doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Reminder with ID '{reminder_id}' not found."
        )
    return ReminderResponse(**doc)

@router.delete("/api/reminders/{reminder_id}", status_code=status.HTTP_200_OK)
def delete_reminder(reminder_id: str):
    """Deletes a scheduled reminder."""
    deleted = ReminderService.delete_reminder(reminder_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Reminder with ID '{reminder_id}' not found."
        )
    return {"success": True, "message": f"Reminder '{reminder_id}' deleted successfully."}

@router.patch("/api/reminders/{reminder_id}/complete", response_model=ReminderResponse)
def toggle_reminder_completion(reminder_id: str, completed: bool = Query(True)):
    """Marks a reminder as completed or pending."""
    doc = ReminderService.mark_completed(reminder_id, completed=completed)
    if not doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Reminder with ID '{reminder_id}' not found."
        )
    return ReminderResponse(**doc)
