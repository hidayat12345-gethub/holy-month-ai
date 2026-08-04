# ============================================
# SETTINGS PAGE
# ============================================

import sys
import os

import streamlit as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from app.core.status import get_health
from app.streamlit import ui

ui.page_header(
    eyebrow="Configuration",
    title="Settings",
    subtitle="Connections and publishing defaults.",
)

config = get_health()

col1, col2 = st.columns(2)
with col1:
    with ui.panel("Connections"):
        st.write(f"Gemini — {'configured' if config.get('gemini') else 'not set'}")
        st.write(f"YouTube — {'configured' if config.get('youtube') else 'not set'}")
        st.write(f"Telegram — {'configured' if config.get('telegram') else 'not set'}")
        st.write(f"FFmpeg — {'found' if config.get('ffmpeg') else 'not found'}")

with col2:
    with ui.panel("Publishing"):
        st.write(f"Publish hour — {config.get('publish_hour', 8)}:00")
        st.write(f"Human review required — {'on' if config.get('require_human_review') else 'off'}")
        st.write("Output folder — output_videos")
        if config.get("ffmpeg"):
            st.caption(config.get("ffmpeg_version", ""))

st.write("")
col1, col2 = st.columns(2)
with col1:
    if st.button("Refresh status", use_container_width=True):
        st.rerun()
with col2:
    if st.button("Show raw status", use_container_width=True):
        st.json(config)
