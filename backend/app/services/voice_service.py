"""Regional-language prompt and recorded-audio lookup utilities."""

import json
from pathlib import Path
from typing import Optional


BASE_DIR = Path(__file__).resolve().parents[2]
CONTENT_DIR = BASE_DIR / "app" / "content"
AUDIO_DIR = BASE_DIR / "audio"

SUPPORTED_LANGUAGES = {
    "en": "English",
    "as": "Assamese",
    "hi": "Hindi",
    "kn": "Kannada",
}


def _prompt_error(language: str, key: str, error: str) -> dict:
    """Build the stable prompt response shape used for client-visible errors."""
    return {
        "success": False,
        "language": language,
        "language_name": SUPPORTED_LANGUAGES.get(language),
        "key": key,
        "text": None,
        "audio_available": False,
        "audio_url": None,
        "tts_fallback_required": False,
        "error": error,
    }


def _content_path(language: str) -> Path:
    return CONTENT_DIR / f"{language}.json"


def _load_language_content(language: str) -> Optional[dict[str, str]]:
    """Load one language's prompt map from its UTF-8 JSON content file."""
    if language not in SUPPORTED_LANGUAGES:
        return None

    content_file = _content_path(language)
    if not content_file.is_file():
        return None

    with content_file.open(encoding="utf-8") as file:
        content = json.load(file)

    if not isinstance(content, dict):
        raise ValueError(f"Voice content for '{language}' must be a JSON object.")

    return content


def get_supported_languages() -> list[dict[str, str]]:
    """Return the language codes and names supported by the Voice Layer."""
    return [
        {"code": code, "name": name}
        for code, name in SUPPORTED_LANGUAGES.items()
        if _content_path(code).is_file()
    ]


def get_voice_text(language: str, key: str) -> Optional[str]:
    """Return translated prompt text for a language and content key."""
    language_content = _load_language_content(language)
    if language_content is None:
        return None

    text = language_content.get(key)
    return text if isinstance(text, str) else None


def get_audio_path(language: str, key: str) -> Optional[Path]:
    """Return the MP3 path when a pre-recorded prompt is available."""
    if language not in SUPPORTED_LANGUAGES or not key.isidentifier():
        return None

    audio_file = AUDIO_DIR / language / f"{key}.mp3"
    return audio_file if audio_file.is_file() else None


def get_voice_prompt(language: str, key: str) -> dict:
    """Return prompt text and recorded-audio/TTS-fallback metadata for the frontend."""
    if language not in SUPPORTED_LANGUAGES:
        return _prompt_error(language, key, "Unsupported language")

    text = get_voice_text(language, key)
    if text is None:
        return _prompt_error(language, key, "Voice content not found")

    audio_available = get_audio_path(language, key) is not None
    return {
        "success": True,
        "language": language,
        "language_name": SUPPORTED_LANGUAGES[language],
        "key": key,
        "text": text,
        "audio_available": audio_available,
        "audio_url": f"/voice/audio/{language}/{key}" if audio_available else None,
        "tts_fallback_required": not audio_available,
    }
