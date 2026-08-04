# ============================================
# UI HELPERS — shared design system components
# ============================================
# Small HTML-snippet builders so every page renders the same
# design tokens instead of copy-pasted inline styles.

import streamlit as st


def stat(value: str, label: str) -> str:
    return (
        f'<div class="hm-stat">'
        f'<div class="hm-stat-value">{value}</div>'
        f'<div class="hm-stat-label">{label}</div>'
        f'</div>'
    )


def stat_row(items: list[tuple[str, str]]):
    """items: list of (value, label)"""
    cols = st.columns(len(items))
    for col, (value, label) in zip(cols, items):
        with col:
            st.markdown(stat(value, label), unsafe_allow_html=True)


def status_pill(label: str, ok: bool, ok_text: str = "Connected", down_text: str = "Not set up") -> str:
    cls = "hm-pill-ok" if ok else "hm-pill-down"
    text = ok_text if ok else down_text
    return f'<div class="hm-pill {cls}"><span class="hm-dot"></span>{label} — {text}</div>'

def status_grid(items: list[tuple[str, bool]]):
    cols = st.columns(len(items))
    for col, (label, ok) in zip(cols, items):
        with col:
            st.markdown(status_pill(label, ok), unsafe_allow_html=True)


def page_header(eyebrow: str, title: str, subtitle: str = ""):
    sub = f'<div class="hm-subtitle">{subtitle}</div>' if subtitle else ""
    st.markdown(
        f'<div class="hm-header">'
        f'<div class="hm-eyebrow">{eyebrow}</div>'
        f'<div class="hm-title">{title}</div>'
        f'{sub}'
        f'</div>',
        unsafe_allow_html=True,
    )


def day_tracker(current_day: int, total_days: int, month_label: str):
    """The signature element — a lunar production calendar strip.
    One video ships per day of the holy month; this shows where
    today sits in that cycle, filled like moon phases waxing."""
    current_day = max(1, min(current_day, total_days))
    dots = "".join(
        f'<span class="hm-day {"hm-day-done" if i < current_day else "hm-day-today" if i == current_day - 1 else ""}"></span>'
        for i in range(total_days)
    )
    st.markdown(
        f'<div class="hm-tracker">'
        f'<div class="hm-tracker-head">'
        f'<span class="hm-tracker-label">{month_label}</span>'
        f'<span class="hm-tracker-count">Day {current_day} <span class="hm-tracker-of">of {total_days}</span></span>'
        f'</div>'
        f'<div class="hm-tracker-strip">{dots}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


def panel(title: str = ""):
    """Bordered panel. Use as: `with ui.panel("Title"): st.write(...)`
    Returns a native st.container so real widgets can be nested inside
    it — a plain markdown div can't contain later widget calls because
    Streamlit renders each call as a sibling, not a child."""
    box = st.container(border=True)
    if title:
        box.markdown(f'<div class="hm-panel-title">{title}</div>', unsafe_allow_html=True)
    return box
