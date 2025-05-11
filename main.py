from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(
    request: Request,
    width: float = Form(...),
    height: float = Form(...),
    color: str = Form(...)
):
    area = round((width * height) / 1_000_000, 2)  # м², если размеры в мм
    return templates.TemplateResponse("form.html", {
        "request": request,
        "width": width,
        "height": height,
        "color": color,
        "area": area
    })