# ============================================
# STREAMLIT DASHBOARD - ENTRY POINT
# ============================================
# This is the file to point Streamlit Cloud at:
#   Main file path: app/streamlit/app.py
#
# Uses st.navigation/st.Page (Streamlit >= 1.36) instead of
# `from pages import 1_Dashboard` — that was invalid Python,
# since module names can't start with a digit.

import os

import streamlit as st

st.set_page_config(
    page_title="Holy Month AI",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="expanded",
)

_css_path = os.path.join(os.path.dirname(__file__), "style.css")
if os.path.exists(_css_path):
    with open(_css_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

_pages_dir = os.path.join(os.path.dirname(__file__), "pages")

pg = st.navigation(
    [
        st.Page(os.path.join(_pages_dir, "1_Dashboard.py"), title="Dashboard", icon=":material/dashboard:", default=True),
        st.Page(os.path.join(_pages_dir, "2_Monthly_Planner.py"), title="Monthly Planner", icon=":material/calendar_month:"),
        st.Page(os.path.join(_pages_dir, "3_Video_Manager.py"), title="Video Manager", icon=":material/movie:"),
        st.Page(os.path.join(_pages_dir, "4_Review_Center.py"), title="Review Center", icon=":material/task_alt:"),
        st.Page(os.path.join(_pages_dir, "5_Analytics.py"), title="Analytics", icon=":material/monitoring:"),
        st.Page(os.path.join(_pages_dir, "6_Settings.py"), title="Settings", icon=":material/tune:"),
    ]
)

with st.sidebar:
    st.markdown(
        """
        <div class="hm-brand">
            <div class="hm-brand-mark">☾</div>
            <div class="hm-brand-name">Holy Month AI</div>
            <div class="hm-brand-sub">Production Desk</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

pg.run()
