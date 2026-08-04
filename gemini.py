# ============================================
# MONTHLY PLANNER PAGE
# ============================================

import sys
import os

import streamlit as st

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from app.streamlit import ui

ui.page_header(
    eyebrow="Planning",
    title="Monthly Planner",
    subtitle="Lay out a month of content in one pass.",
)

with st.form("create_plan_form"):
    col1, col2 = st.columns(2)
    with col1:
        theme = st.selectbox("Theme", ["ramadan", "rabi_al_awwal", "muharram", "general_islamic"])
        holy_month = st.text_input("Holy month", "Rabi' al-Awwal")
    with col2:
        language = st.selectbox("Language", ["en", "ur", "ar"])
        audience = st.text_input("Audience", "young adults")

    total_videos = st.slider("Videos in this plan", 5, 30, 30)

    submitted = st.form_submit_button("Create plan", use_container_width=True)

    if submitted:
        # NOTE: stub — wire this to a real Plan row (app.models.plan.Plan
        # + a DB session) once the planning agent is built. For now it
        # just confirms what you entered.
        st.success("Plan captured.")
        st.json(
            {
                "theme": theme,
                "holy_month": holy_month,
                "target_audience": audience,
                "preferred_language": language,
                "total_videos": total_videos,
            }
        )

st.write("")
st.markdown("#### Existing plans")
st.info("No plans yet. Plan storage isn't wired up in this build — create one above to see the captured fields.")
