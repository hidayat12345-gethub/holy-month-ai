# ============================================
# CONFIGURATION
# ============================================
# Reads settings from (in priority order):
#   1. Streamlit Cloud "Secrets" (st.secrets)      <- used when deployed
#   2. A local .env file (python-dotenv)            <- used for local dev
# This lets the exact same code run locally and on Streamlit Cloud.

import os
from dotenv import load_dotenv

load_dotenv()


def _get(key: str, default: str = "") -> str:
    """Look in Streamlit secrets first (if available), then env vars."""
    try:
        import streamlit as st
        if key in st.secrets:
            return str(st.secrets[key])
    except Exception:
        pass
    return os.getenv(key, default)


class Settings:
    """Application settings."""

    # Gemini
    GEMINI_API_KEY = _get("GEMINI_API_KEY", "")
    GEMINI_MODEL = _get("GEMINI_MODEL", "gemini-2.5-flash")

    # YouTube
    YOUTUBE_CLIENT_ID = _get("YOUTUBE_CLIENT_ID", "")
    YOUTUBE_CLIENT_SECRET = _get("YOUTUBE_CLIENT_SECRET", "")
    YOUTUBE_REFRESH_TOKEN = _get("YOUTUBE_REFRESH_TOKEN", "")

    # Telegram
    TELEGRAM_BOT_TOKEN = _get("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID = _get("TELEGRAM_CHAT_ID", "")

    # FFmpeg — leave blank on Linux/Streamlit Cloud, it's found on PATH
    # automatically once packages.txt installs it.
    FFMPEG_PATH = _get("FFMPEG_PATH", "")

    # System
    DATABASE_URL = _get("DATABASE_URL", "sqlite:///./holy_month.db")
    OUTPUT_FOLDER = _get("OUTPUT_FOLDER", "output_videos")
    PUBLISH_HOUR = int(_get("PUBLISH_HOUR", "8"))
    REQUIRE_HUMAN_REVIEW = str(_get("REQUIRE_HUMAN_REVIEW", "true")).lower() == "true"

    @property
    def is_gemini_configured(self):
        return bool(self.GEMINI_API_KEY)

    @property
    def is_youtube_configured(self):
        return bool(self.YOUTUBE_CLIENT_ID and self.YOUTUBE_CLIENT_SECRET)

    @property
    def is_telegram_configured(self):
        return bool(self.TELEGRAM_BOT_TOKEN and self.TELEGRAM_CHAT_ID)

    @property
    def is_ffmpeg_configured(self):
        import shutil
        if self.FFMPEG_PATH:
            return os.path.exists(self.FFMPEG_PATH)
        return shutil.which("ffmpeg") is not None


settings = Settings()
