/* ============================================
   HOLY MONTH AI — DESIGN SYSTEM
   ============================================
   Direction: an editorial production desk, not a SaaS-purple
   dashboard. Deep night-indigo surface, brass/lantern gold as
   the single accent, a serif display face for editorial weight,
   Inter for body text, and a mono face for anything that reads
   like data (counts, timestamps, statuses) — the vocabulary of
   a broadcast control room.
*/

@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,440;9..144,560;9..144,650&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg-deep: #0A0E17;
    --bg-panel: #121826;
    --bg-raised: #171F30;
    --border: rgba(233, 227, 213, 0.09);
    --border-strong: rgba(233, 227, 213, 0.18);
    --gold: #C89A4C;
    --gold-soft: #E4C583;
    --ink: #ECE8DE;
    --muted: #8B93A6;
    --faint: #565E72;
    --success: #4FAE7C;
    --warning: #E0A83E;
    --danger: #D9695A;
    --font-display: 'Fraunces', Georgia, serif;
    --font-body: 'Inter', -apple-system, sans-serif;
    --font-mono: 'JetBrains Mono', ui-monospace, monospace;
}

/* ---------- base ---------- */
.stApp {
    background: var(--bg-deep);
    font-family: var(--font-body);
    color: var(--ink);
}
html, body, [class*="css"] { font-family: var(--font-body); }
h1, h2, h3 { font-family: var(--font-display); letter-spacing: -0.01em; }

.block-container { padding-top: 2.25rem; max-width: 1180px; }

/* subtle top hairline instead of a big colored band */
.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border-strong) 30%, var(--border-strong) 70%, transparent);
    z-index: 999;
}

/* ---------- sidebar ---------- */
[data-testid="stSidebar"] {
    background: var(--bg-panel);
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] * { font-family: var(--font-body); }

.hm-brand {
    padding: 28px 8px 18px 8px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 6px;
}
.hm-brand-mark {
    font-family: var(--font-display);
    font-size: 1.9rem;
    color: var(--gold-soft);
    line-height: 1;
}
.hm-brand-name {
    font-family: var(--font-display);
    font-size: 1.05rem;
    font-weight: 560;
    color: var(--ink);
    margin-top: 6px;
}
.hm-brand-sub {
    font-family: var(--font-mono);
    font-size: 0.68rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--faint);
    margin-top: 2px;
}

/* Streamlit's native nav (st.navigation) */
[data-testid="stSidebarNav"] a,
[data-testid="stSidebarNavLink"] {
    font-family: var(--font-body) !important;
    font-size: 0.92rem !important;
    border-radius: 6px !important;
    border-left: 2px solid transparent;
    color: var(--muted) !important;
}
[data-testid="stSidebarNav"] a:hover {
    background: var(--bg-raised) !important;
    color: var(--ink) !important;
}
[data-testid="stSidebarNav"] a[aria-current="page"],
[data-testid="stSidebarNavLink"][aria-current="page"] {
    background: var(--bg-raised) !important;
    border-left: 2px solid var(--gold);
    color: var(--gold-soft) !important;
    font-weight: 600 !important;
}

/* ---------- headers ---------- */
.hm-eyebrow {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--gold-soft);
    margin-bottom: 6px;
}
.hm-title {
    font-family: var(--font-display);
    font-size: 2.1rem;
    font-weight: 560;
    color: var(--ink);
    line-height: 1.15;
}
.hm-subtitle {
    font-family: var(--font-body);
    color: var(--muted);
    font-size: 0.95rem;
    margin-top: 6px;
}
.hm-header { margin-bottom: 1.75rem; padding-bottom: 1.25rem; border-bottom: 1px solid var(--border); }

/* ---------- stat cards ---------- */
.hm-stat {
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px 20px;
}
.hm-stat-value {
    font-family: var(--font-mono);
    font-size: 1.9rem;
    font-weight: 600;
    color: var(--ink);
    line-height: 1;
}
.hm-stat-label {
    font-family: var(--font-body);
    font-size: 0.8rem;
    color: var(--muted);
    margin-top: 8px;
}

/* ---------- status pills ---------- */
.hm-pill {
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 14px;
    font-size: 0.82rem;
    color: var(--muted);
    display: flex;
    align-items: center;
    gap: 8px;
}
.hm-dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }
.hm-pill-ok .hm-dot { background: var(--success); box-shadow: 0 0 6px rgba(79,174,124,0.6); }
.hm-pill-ok { color: var(--ink); border-color: rgba(79,174,124,0.25); }
.hm-pill-down .hm-dot { background: var(--faint); }
.hm-pill-down { color: var(--faint); }

/* ---------- day tracker (signature element) ---------- */
.hm-tracker {
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px 20px 20px 20px;
    margin-bottom: 1.75rem;
}
.hm-tracker-head { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 14px; }
.hm-tracker-label { font-family: var(--font-body); font-size: 0.85rem; color: var(--muted); }
.hm-tracker-count { font-family: var(--font-mono); font-size: 1rem; color: var(--gold-soft); font-weight: 600; }
.hm-tracker-of { color: var(--faint); font-weight: 400; }
.hm-tracker-strip { display: flex; gap: 4px; flex-wrap: wrap; }
.hm-day {
    width: 100%;
    max-width: 22px;
    height: 8px;
    border-radius: 2px;
    background: var(--border-strong);
    flex: 1 1 0;
}
.hm-day-done { background: var(--gold); opacity: 0.55; }
.hm-day-today { background: var(--gold-soft); box-shadow: 0 0 8px rgba(228,197,131,0.7); }

/* ---------- generic panel ---------- */
.hm-panel-title {
    font-family: var(--font-display);
    font-size: 1.05rem;
    font-weight: 560;
    color: var(--ink);
    margin-bottom: 10px;
}
div[data-testid="stVerticalBlockBorderWrapper"] > div {
    background: var(--bg-panel);
}
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: var(--border) !important;
    border-radius: 10px !important;
}

/* ---------- buttons ---------- */
.stButton > button {
    background: var(--bg-raised);
    color: var(--ink);
    border: 1px solid var(--border-strong);
    border-radius: 7px;
    padding: 8px 18px;
    font-family: var(--font-body);
    font-weight: 500;
    font-size: 0.88rem;
    transition: border-color 0.15s ease, color 0.15s ease;
}
.stButton > button:hover {
    border-color: var(--gold);
    color: var(--gold-soft);
}
.stButton > button[kind="primary"] {
    background: var(--gold);
    border-color: var(--gold);
    color: #17130A;
}
.stFormSubmitButton button {
    font-weight: 600;
}
.stFormSubmitButton button {
    background: var(--gold) !important;
    border-color: var(--gold) !important;
    color: #17130A !important;
}
.stFormSubmitButton button:hover {
    background: var(--gold-soft) !important;
    border-color: var(--gold-soft) !important;
}

/* ---------- inputs ---------- */
.stTextInput input, .stSelectbox div[data-baseweb="select"], .stTextArea textarea {
    background: var(--bg-raised) !important;
    border: 1px solid var(--border-strong) !important;
    color: var(--ink) !important;
    border-radius: 7px !important;
}
.stSlider [data-baseweb="slider"] div[role="slider"] { background: var(--gold) !important; }
.stSlider [data-baseweb="slider"] > div > div { background: var(--gold) !important; }

/* ---------- misc native components ---------- */
[data-testid="metric-container"] {
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px;
}
.streamlit-expanderHeader { background: var(--bg-panel); border-radius: 8px; }
[data-testid="stForm"] {
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 22px;
}
hr { border-color: var(--border); }
[data-testid="stCaptionContainer"] { color: var(--faint); font-family: var(--font-mono); font-size: 0.72rem; }

/* alerts — keep semantic colors but on-brand surfaces */
[data-testid="stAlert"] { border-radius: 8px; border: 1px solid var(--border); }
