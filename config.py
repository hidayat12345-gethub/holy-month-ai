# ============================================
# LOCAL DEV RUNNER (FastAPI + Streamlit)
# ============================================
# OPTIONAL — only used if you want a FastAPI backend running
# alongside Streamlit on your own machine. Streamlit Community
# Cloud does NOT run this file — it runs app/streamlit/app.py
# directly as a single process. Keep this only if you plan to
# build out real API endpoints for other clients later.

import os
import sys
import threading
import subprocess
from contextlib import asynccontextmanager

from fastapi import FastAPI

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config import settings
from app.core.status import get_health


@asynccontextmanager
async def lifespan(app: FastAPI):
    os.makedirs(settings.OUTPUT_FOLDER, exist_ok=True)
    print("🕌 Holy Month AI backend starting up...")
    yield
    print("🕌 Holy Month AI backend shutting down...")


app = FastAPI(
    title="Holy Month AI - YouTube Automation",
    version="2.0.0",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {"name": "Holy Month AI", "version": "2.0.0", "status": "running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "config": get_health()}


def run_streamlit():
    streamlit_path = os.path.join(os.path.dirname(__file__), "streamlit", "app.py")
    subprocess.run([sys.executable, "-m", "streamlit", "run", streamlit_path])


def run_fastapi():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    fastapi_thread = threading.Thread(target=run_fastapi, daemon=True)
    streamlit_thread = threading.Thread(target=run_streamlit, daemon=True)

    fastapi_thread.start()
    streamlit_thread.start()

    print("\n🚀 Both servers are running!")
    print("📊 Streamlit: http://localhost:8501")
    print("🔗 FastAPI:   http://localhost:8000")

    try:
        fastapi_thread.join()
        streamlit_thread.join()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
