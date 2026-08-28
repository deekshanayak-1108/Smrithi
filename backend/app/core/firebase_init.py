import os
import json
import logging
import firebase_admin
from firebase_admin import credentials, firestore
from app.core.config import FIREBASE_CRED_PATH

logger = logging.getLogger("uvicorn")

db = None

def init_firebase():
    global db
    if firebase_admin._apps:
        try:
            db = firestore.client()
        except Exception:
            db = None
        return

    if os.path.exists(FIREBASE_CRED_PATH) and os.path.getsize(FIREBASE_CRED_PATH) > 0:
        try:
            cred = credentials.Certificate(FIREBASE_CRED_PATH)
            firebase_admin.initialize_app(cred)
            logger.info(f"Firebase Admin SDK initialized using '{FIREBASE_CRED_PATH}'.")
        except (json.JSONDecodeError, ValueError, Exception) as e:
            logger.warning(
                f"Could not load Firebase credentials from '{FIREBASE_CRED_PATH}' ({e}). "
                "Attempting default app initialization..."
            )
            try:
                firebase_admin.initialize_app()
            except Exception as init_err:
                logger.warning(f"Default Firebase app initialization failed: {init_err}")
    else:
        logger.warning(
            f"Firebase credential file '{FIREBASE_CRED_PATH}' is missing or empty. "
            "Attempting default app initialization..."
        )
        try:
            firebase_admin.initialize_app()
        except Exception as init_err:
            logger.warning(f"Default Firebase app initialization failed: {init_err}")

    try:
        db = firestore.client()
    except Exception as e:
        logger.warning(f"Firestore client initialization failed: {e}")
        db = None

init_firebase()