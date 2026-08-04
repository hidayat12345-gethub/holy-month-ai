# ============================================
# VIDEO MANAGER PAGE
# ============================================

import sys
import os

import streamlit as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from app.streamlit import ui

ui.page_header(
    eyebrow="Production",
    title="Video Manager",
    subtitle="Every video the pipeline has produced, in one list.",
)

st.info("No videos yet. Generation and storage aren't wired up in this build.")
