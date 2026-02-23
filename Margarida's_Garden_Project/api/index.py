"""
Vercel Serverless entry for FastAPI.
"""
import sys
from pathlib import Path

# Adiciona backend ao path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "backend"))

from app.main import app
