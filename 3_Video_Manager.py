# ============================================
# ANALYTICS PAGE
# ============================================

import sys
import os

import streamlit as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from app.streamlit import ui

ui.page_header(
    eyebrow="Performance",
    title="Analytics",
    subtitle="How published videos are doing.",
)

ui.stat_row(
    [
        ("0", "Videos"),
        ("0", "Views"),
        ("0", "Subscribers gained"),
        ("0 hrs", "Watch time"),
    ]
)

st.write("")
st.info("Charts appear here once you've published videos.")
