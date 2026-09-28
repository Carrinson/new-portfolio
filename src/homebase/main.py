from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from homebase.content import PROJECTS

app = FastAPI(
    title="My portfolio", description="This is my portfolio website", version="1.0.0"
)


# __file__ is this module's own path. Path() turns it into a path object,
# .resolve() makes it absolute (and follows symlinks), .parent drops the
# filename and leaves the folder that main.py lives in.
# Result: an absolute path that never depends on where you launched uvicorn.
BASE_DIR = Path(__file__).resolve().parent

# BASE_DIR / "static" joins path segments. Path's / operator emits the
# correct separator for the OS, so this is \ on Windows and / on Ubuntu.
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Same fix for templates: absolute path, resolved from the module's location.
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"projects": PROJECTS})


@app.get("/healthz")
async def get_health():
    return {"status": "ok"}
