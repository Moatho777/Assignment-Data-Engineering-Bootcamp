from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

# استدعاء دالة البحث
from similarity.similarity import search_name

app = FastAPI()

# ربط المجلدات
templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "results": None})

@app.post("/search", response_class=HTMLResponse)
async def search(request: Request, query: str = Form(...)):
    results = search_name(query)
    return templates.TemplateResponse("index.html", {"request": request, "results": results, "query": query})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
