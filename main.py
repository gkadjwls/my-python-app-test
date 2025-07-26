from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 템플릿 폴더 설정
templates = Jinja2Templates(directory="app/templates")

# 정적 파일 (필요 시 사용 가능)
# app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    # index.html 템플릿 렌더링
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
