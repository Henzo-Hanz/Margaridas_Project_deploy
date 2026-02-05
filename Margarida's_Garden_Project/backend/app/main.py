"""Aplicação principal - Margarida's Garden."""
import logging
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, credentials
from app.core.database import engine, Base
from app.core.config import BASE_DIR

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("margarida_garden")

app = FastAPI(
    title="Margarida's Garden",
    description="Gerenciador de senhas amigável e seguro",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas API
app.include_router(auth.router, prefix="/api")
app.include_router(credentials.router, prefix="/api")

# Diretórios estáticos e templates
STATIC_DIR = BASE_DIR / "frontend" / "static"
TEMPLATES_DIR = BASE_DIR / "frontend" / "templates"

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@app.on_event("startup")
def startup():
    """Cria tabelas no banco ao iniciar."""
    Base.metadata.create_all(bind=engine)
    logger.info("Margarida's Garden iniciado")


@app.get("/")
async def homepage(request: Request):
    """Landing page - jardim de senhas."""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "user_name": "Margarida",  # V1: usuário fixo
            "flower_colors": ["pink", "yellow", "purple", "rose", "peach", "lavender", "pink"],
        },
    )


@app.get("/login")
async def login_page(request: Request):
    """Página de login."""
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/garden")
async def garden_page(request: Request):
    """Página do jardim - gerenciamento de senhas (requer auth)."""
    return templates.TemplateResponse("garden.html", {"request": request})
