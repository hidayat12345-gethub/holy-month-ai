# ============================================
# DASHBOARD PAGE
# ============================================

import sys
import os

import streamlit as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from app.core.status import get_health
from app.core.gemini import gemini_service
from app.streamlit import ui

ui.page_header(
    eyebrow="Overview",
    title="Dashboard",
    subtitle="Where today's production cycle stands.",
)

config = get_health()

# Signature element: production calendar. No plan exists yet in this
# build, so it's shown empty rather than faked — see Monthly Planner.
ui.day_tracker(current_day=0, total_days=30, month_label="No active production plan")

ui.stat_row(
    [
        ("0", "Videos produced"),
        ("0", "Published"),
        ("0", "Awaiting review"),
        ("0", "Scheduled"),
    ]
)

st.write("")
st.markdown("#### Connections")
ui.status_grid(
    [
        ("Gemini", config.get("gemini")),
        ("YouTube", config.get("youtube")),
        ("Telegram", config.get("telegram")),
        ("FFmpeg", config.get("ffmpeg")),
        ("Database", True),
    ]
)
if config.get("ffmpeg"):
    st.caption(config.get("ffmpeg_version", ""))

st.write("")
st.markdown("#### Start here")

col1, col2, col3 = st.columns(3)

with col1:
    with ui.panel():
        st.markdown("**Create a plan**")
        st.caption("Set a theme and length, and lay out the month.")
        if st.button("Open Monthly Planner", use_container_width=True):
            st.switch_page(os.path.join(os.path.dirname(__file__), "2_Monthly_Planner.py"))

with col2:
    with ui.panel():
        st.markdown("**Check Gemini**")
        st.caption("Send a test prompt and confirm the key works.")
        if st.button("Run test script", use_container_width=True):
            if not config.get("gemini"):
                st.error("Add GEMINI_API_KEY in Settings → Secrets first.")
            else:
                with st.spinner("Generating..."):
                    result = gemini_service.generate_script(
                        theme="ramadan",
                        holy_month="Ramadan",
                        language="en",
                        audience="young adults",
                    )
                if result.get("success"):
                    st.success("Gemini responded.")
                    with st.expander("Show script"):
                        st.write(result["script"])
                else:
                    st.error(result.get("error", "Unknown error"))

with col3:
    with ui.panel():
        st.markdown("**Refresh status**")
        st.caption("Re-check every connection above.")
        if st.button("Refresh", use_container_width=True):
            st.rerun()
