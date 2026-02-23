"""Aplicação principal - Margarida's Garden."""
import logging
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.api import auth, credentials, treasury
from app.core.rate_limit import limiter
from app.core.database import engine, Base
from app.core.config import settings
from app.core.middlewares import SecurityHeadersMiddleware

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("margarida_garden")

app = FastAPI(
    title="Margarida's Garden & Treasury",
    description="Gerenciador de senhas e finanças pessoais",
    version="2.0.0",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        logger.error("Unhandled exception: %s", e, exc_info=True)
        detail = "Internal server error" if settings.is_production else str(e)
        return JSONResponse(status_code=500, content={"detail": detail})

# Rotas API
app.include_router(auth.router, prefix="/api")
app.include_router(credentials.router, prefix="/api")
app.include_router(treasury.router, prefix="/api")

# Diretórios estáticos e templates
STATIC_DIR = settings.BASE_DIR / "frontend" / "static"
TEMPLATES_DIR = settings.BASE_DIR / "frontend" / "templates"

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@app.on_event("startup")
def startup():
    """Cria tabelas no banco ao iniciar.

    O método original apenas garante que as tabelas existem. Em
    ambientes serverless (como Vercel) também é conveniente criar o
    usuário padrão usado nos testes/development. Esse comportamento
    substitui o script `backend/scripts/init_db.py` quando a aplicação
    sobe no serviço.
    """
    settings.require_secret_key_in_production()

    # cria todas as tabelas (migrations simples)
    Base.metadata.create_all(bind=engine)

    # usuário padrão
    try:
        from app.core.security import get_password_hash
        from app.models.user import User
        from app.core.database import SessionLocal

        db = SessionLocal()
        if not db.query(User).filter(User.email == settings.DEFAULT_USER_EMAIL).first():
            user = User(
                name=settings.DEFAULT_USER_NAME,
                email=settings.DEFAULT_USER_EMAIL,
                hashed_password=get_password_hash(settings.DEFAULT_USER_PASSWORD),
            )
            db.add(user)
            db.commit()
            logger.info("Usuário padrão '%s' criado no banco", settings.DEFAULT_USER_EMAIL)
    except Exception:  # pragma: no cover - não quer falhar startup
        logger.exception("Erro ao criar usuário padrão")
    finally:
        try:
            db.close()
        except Exception:  # type: ignore
            pass

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


@app.get("/dashboard")
async def dashboard_page(request: Request):
    """Página de seleção entre aplicativos (intermediária após login)."""
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/treasury")
async def treasury_page(request: Request):
    """Página do Treasury - gerenciamento de finanças (requer auth)."""
    return templates.TemplateResponse("treasury.html", {"request": request})
