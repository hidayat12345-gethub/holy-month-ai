# ============================================
# REVIEW CENTER PAGE
# ============================================

import sys
import os

import streamlit as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from app.streamlit import ui

ui.page_header(
    eyebrow="Quality gate",
    title="Review Center",
    subtitle="Nothing publishes until it's approved here.",
)

st.markdown("Once videos start generating, each one lands here before it goes live. From this screen you'll be able to:")
st.markdown(
    """
- Preview the video before it publishes
- Approve it, or reject it with a note
- Edit the title and description
- Set a publish time
"""
)

st.write("")
st.markdown("#### Awaiting review")
st.info("Nothing pending. Generate a video first.")
