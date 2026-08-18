from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from backend.database import init_db, async_session
from backend.services.chapter_service import seed_chapters
from backend.routes import auth, chapters, progress, dashboard



@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    async with async_session() as db:
        await seed_chapters(db)
    yield


app = FastAPI(title="How Cybersecurity Works", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(chapters.router)
app.include_router(progress.router)
app.include_router(dashboard.router)


app.mount("/css", StaticFiles(directory="frontend/css"), name="css")
app.mount("/js", StaticFiles(directory="frontend/js"), name="js")
app.mount("/assets", StaticFiles(directory="frontend/assets"), name="assets")


@app.get("/")
@app.get("/login")
@app.get("/register")
@app.get("/home")
@app.get("/library")
@app.get("/progress")
@app.get("/quiz")
@app.get("/read/{path:path}")
async def serve_spa(path: str = ""):
    return FileResponse("frontend/index.html")


@app.get("/api/health")
async def health():
    return {"status": "ok", "app": "How Cybersecurity Works"}
