import unittest

from fastapi.testclient import TestClient

from app.main import app


class VoiceEndpointTests(unittest.TestCase):
    client = TestClient(app)
    prompt_fields = {
        "success",
        "language",
        "language_name",
        "key",
        "text",
        "audio_available",
        "audio_url",
        "tts_fallback_required",
    }

    def assert_prompt_shape(self, payload: dict) -> None:
        self.assertTrue(self.prompt_fields.issubset(payload))

    def test_supported_languages(self) -> None:
        response = self.client.get("/voice/languages")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["languages"],
            [
                {"code": "en", "name": "English"},
                {"code": "as", "name": "Assamese"},
                {"code": "hi", "name": "Hindi"},
                {"code": "kn", "name": "Kannada"},
            ],
        )

    def test_english_prompt_prefers_existing_audio(self) -> None:
        response = self.client.get("/voice/prompt/en/welcome")
        payload = response.json()

        self.assertEqual(response.status_code, 200)
        self.assert_prompt_shape(payload)
        self.assertEqual(payload["text"], "Welcome to Smrithi.")
        self.assertTrue(payload["audio_available"])
        self.assertEqual(payload["audio_url"], "/voice/audio/en/welcome")
        self.assertFalse(payload["tts_fallback_required"])

    def test_assamese_prompt_uses_tts_fallback_without_audio(self) -> None:
        response = self.client.get("/voice/prompt/as/welcome")
        payload = response.json()

        self.assertEqual(response.status_code, 200)
        self.assert_prompt_shape(payload)
        self.assertEqual(payload["text"], "স্মৃতিলৈ স্বাগতম।")
        self.assertFalse(payload["audio_available"])
        self.assertIsNone(payload["audio_url"])
        self.assertTrue(payload["tts_fallback_required"])

    def test_hindi_prompt_uses_tts_fallback_without_audio(self) -> None:
        response = self.client.get("/voice/prompt/hi/welcome")
        payload = response.json()

        self.assertEqual(response.status_code, 200)
        self.assert_prompt_shape(payload)
        self.assertEqual(payload["text"], "स्मृति में आपका स्वागत है।")
        self.assertFalse(payload["audio_available"])
        self.assertIsNone(payload["audio_url"])
        self.assertTrue(payload["tts_fallback_required"])

    def test_kannada_prompt_uses_tts_fallback_without_audio(self) -> None:
        response = self.client.get("/voice/prompt/kn/welcome")
        payload = response.json()

        self.assertEqual(response.status_code, 200)
        self.assert_prompt_shape(payload)
        self.assertEqual(payload["text"], "ಸ್ಮೃತಿಗೆ ಸ್ವಾಗತ.")
        self.assertFalse(payload["audio_available"])
        self.assertIsNone(payload["audio_url"])
        self.assertTrue(payload["tts_fallback_required"])

    def test_existing_english_audio_is_served(self) -> None:
        response = self.client.get("/voice/audio/en/welcome")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "audio/mpeg")

    def test_missing_prompt_returns_consistent_404_response(self) -> None:
        response = self.client.get("/voice/prompt/en/not_a_prompt")
        payload = response.json()

        self.assertEqual(response.status_code, 404)
        self.assert_prompt_shape(payload)
        self.assertFalse(payload["success"])
        self.assertEqual(payload["error"], "Voice content not found")

    def test_unsupported_language_returns_consistent_404_response(self) -> None:
        response = self.client.get("/voice/prompt/fr/welcome")
        payload = response.json()

        self.assertEqual(response.status_code, 404)
        self.assert_prompt_shape(payload)
        self.assertFalse(payload["success"])
        self.assertEqual(payload["error"], "Unsupported language")

    def test_missing_audio_returns_404(self) -> None:
        response = self.client.get("/voice/audio/as/welcome")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "Audio file not found")


if __name__ == "__main__":
    unittest.main()
