from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, JSONResponse

from app.services.voice_service import (
    get_supported_languages,
    get_voice_prompt,
    get_audio_path,
)


router = APIRouter(prefix="/voice", tags=["voice"])


# ---------------------------------------------------------
# GET SUPPORTED LANGUAGES
# ---------------------------------------------------------

@router.get("/languages")
def languages():
    return {
        "languages": get_supported_languages()
    }


# ---------------------------------------------------------
# GET VOICE PROMPT
# ---------------------------------------------------------

@router.get("/prompt/{language}/{key}")
def voice_prompt(
    language: str,
    key: str,
):
    result = get_voice_prompt(
        language=language,
        key=key,
    )

    if not result["success"]:
        return JSONResponse(status_code=404, content=result)

    return result


# ---------------------------------------------------------
# GET AUDIO FILE
# ---------------------------------------------------------

@router.get("/audio/{language}/{key}")
def voice_audio(
    language: str,
    key: str,
):
    """
    Return a pre-recorded audio file.

    Example:

    /voice/audio/en/welcome

    /voice/audio/as/remember_objects
    """

    prompt = get_voice_prompt(language=language, key=key)
    if not prompt["success"]:
        raise HTTPException(status_code=404, detail=prompt["error"])

    audio_path = get_audio_path(language=language, key=key)

    if audio_path is None:
        raise HTTPException(
            status_code=404,
            detail="Audio file not found",
        )

    return FileResponse(
        path=audio_path,
        media_type="audio/mpeg",
        filename=f"{key}.mp3",
    )
