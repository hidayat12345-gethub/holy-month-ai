# 🕌 Holy Month AI - YouTube Automation

AI-powered YouTube automation for Islamic holy months, with a Streamlit dashboard.

## ✨ Features

- 🤖 AI-generated video scripts with Google Gemini
- 📅 Monthly content planning form
- 🎬 FFmpeg-based video pipeline (helpers included, not yet wired to a full agent)
- 📤 YouTube upload helpers (Data API, OAuth refresh token)
- 📱 Telegram notification config
- 👀 Human-review gate flag
- 📊 Streamlit dashboard (single deployable app)

## 🚀 Run locally

```bash
git clone https://github.com/yourusername/holy_month_ai.git
cd holy_month_ai

pip install -r requirements.txt
# Also install ffmpeg on your system and make sure it's on PATH
# (Windows: download it and either add to PATH or set FFMPEG_PATH in .env)

cp .env.example .env
# edit .env with your real keys

streamlit run app/streamlit/app.py
```

Dashboard opens at `http://localhost:8501`.

(Optional) If you also want the FastAPI backend running locally for future API work:
```bash
python -m app.main
```

## ☁️ Deploy live on Streamlit Community Cloud

1. Push this folder to a **public or private GitHub repo**. Do **not** commit `.env` — it's already in `.gitignore`.
2. Go to https://share.streamlit.io and click **"New app"**.
3. Pick your repo/branch, and set **Main file path** to:
   ```
   app/streamlit/app.py
   ```
4. Before deploying (or after, in **Settings → Secrets**), paste your real keys using the format in `.streamlit/secrets.toml.example`. Streamlit Cloud secrets are read automatically by `app/config.py` — you don't need a `.env` file there.
5. Deploy. `packages.txt` tells Streamlit Cloud to install the `ffmpeg` system binary automatically.

## 📁 Structure

```
holy_month_ai/
├── .env.example              # copy to .env for local dev (never commit .env)
├── .streamlit/
│   ├── config.toml           # theme (Streamlit only reads config from here)
│   └── secrets.toml.example  # copy content into Streamlit Cloud's Secrets panel
├── .gitignore
├── packages.txt              # apt packages for Streamlit Cloud (ffmpeg)
├── requirements.txt
├── README.md
└── app/
    ├── config.py              # reads st.secrets first, then .env
    ├── main.py                 # OPTIONAL local FastAPI+Streamlit runner
    ├── core/
    │   ├── database.py
    │   ├── gemini.py
    │   ├── ffmpeg.py
    │   └── status.py           # system status, used directly by pages
    ├── models/
    │   ├── plan.py
    │   └── video.py
    └── streamlit/
        ├── app.py               # <- Streamlit Cloud entry point
        ├── style.css
        └── pages/
            ├── 1_Dashboard.py
            ├── 2_Monthly_Planner.py
            ├── 3_Video_Manager.py
            ├── 4_Review_Center.py
            ├── 5_Analytics.py
            └── 6_Settings.py
```

## 🔑 Environment variables / secrets

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Gemini AI API key |
| `GEMINI_MODEL` | Gemini model (`gemini-2.5-flash`) |
| `YOUTUBE_CLIENT_ID` | YouTube OAuth client ID |
| `YOUTUBE_CLIENT_SECRET` | YouTube OAuth secret |
| `YOUTUBE_REFRESH_TOKEN` | YouTube refresh token |
| `TELEGRAM_BOT_TOKEN` | Telegram bot token |
| `TELEGRAM_CHAT_ID` | Telegram chat ID |
| `FFMPEG_PATH` | Only needed on Windows if ffmpeg isn't on PATH — leave blank on Streamlit Cloud |

## 🛠 What was fixed vs. the original file dump

1. **App crash on startup**: `from pages import 1_Dashboard as page` is invalid Python — module names can't start with a digit. Replaced the whole manual-import/`show()` pattern with Streamlit's native `st.navigation` + `st.Page`, which loads pages by file path instead of import.
2. **Wouldn't actually go live on Streamlit Cloud**: the original architecture required a separate FastAPI server on `localhost:8000` that the Streamlit pages called over HTTP. Streamlit Community Cloud only runs *one* process (your Streamlit main file) — the FastAPI server would never be reachable, so every page would show "Cannot connect to API". Pages now call `app/core/*` services directly in-process. `app/main.py` (FastAPI) is kept only as an optional local-dev extra.
3. **`streamlit.toml` at repo root does nothing** — Streamlit only reads config from `.streamlit/config.toml`. Moved it there.
4. **Secrets on Streamlit Cloud**: there's no `.env` file in that environment. Added `.streamlit/secrets.toml.example` and made `app/config.py` read `st.secrets` first, falling back to `.env`/`os.getenv` for local dev — same code works in both places.
5. **`FFMPEG_PATH` defaulted to a Windows path** (`C:\ffmpeg\bin\ffmpeg.exe`), which is meaningless on Streamlit Cloud's Linux containers and would silently make ffmpeg look "unconfigured". Default is now blank, and `packages.txt` installs the real `ffmpeg` binary via apt so `shutil.which("ffmpeg")` finds it automatically.
6. **Deprecated SQLAlchemy import** (`from sqlalchemy.ext.declarative import declarative_base`) — updated to `from sqlalchemy.orm import declarative_base` (SQLAlchemy 2.x).
7. **Trimmed `requirements.txt`** to only what the code actually imports (dropped `moviepy`, `opencv-python-headless`, `apscheduler`, `alembic`, `gunicorn`, `loguru`, `numpy`, `pydantic-settings`, `python-multipart` — none were used anywhere in the given files). This keeps the Streamlit Cloud build fast and less likely to hit memory/build-time limits on the free tier. Add any of these back in `requirements.txt` if/when you actually build the features that need them.
8. **Deprecated Gemini SDK**: `google-generativeai` has ended support upstream. Switched `app/core/gemini.py` to the current `google-genai` package/client API.
9. **`.streamlit/config.toml`** had `enableCORS = false` together with `enableXsrfProtection = true`, which Streamlit silently overrides (and warns about) since that combo isn't valid — removed the conflicting line.
10. **`.gitignore`** now also excludes `.streamlit/secrets.toml` (only the `.example` version should ever be committed), and no longer blanket-ignores all `*.png`/`*.jpg` repo-wide (that would've also hidden things like a logo you might want to commit) — narrowed to `output_videos/`.

## ⚠️ Still stubbed (by design, not a bug)

The Monthly Planner, Video Manager, and Analytics pages don't yet read/write the database — they're UI shells, same as in the original file dump. Plan/Video creation just echoes back what you entered. Wiring these to real `Plan`/`Video` rows and the actual generation pipeline is the next phase.

## 🎨 Visual design

Restyled from the default purple-SaaS template look to an editorial
"production desk" theme: deep indigo surface, a single brass/gold
accent, Fraunces for headings, Inter for body text, and JetBrains
Mono for anything numeric (counts, statuses, timestamps). The
signature element on the Dashboard is a lunar day-tracker strip —
since the product ships one video per day of a holy month, the
tracker shows where today sits in that cycle, empty until a plan
exists.

Shared components live in `app/streamlit/ui.py` (`page_header`,
`stat_row`, `status_grid`, `day_tracker`, `panel`) so every page
pulls from the same design tokens in `style.css` instead of
duplicating inline styles.
