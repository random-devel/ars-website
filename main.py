from fastapi import FastAPI, Depends, status
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.exception_handler(404)
async def not_found(request: Request, exc: HTTPException):
    return HTMLResponse(
        content=open("html/404.html").read(),
        status_code=404
    )

@app.get('/')
def root():
    return FileResponse('html/index.html')

@app.get('/login')
def log():
    return FileResponse('html/login.html')

@app.get('/store')
def sotre():
    return FileResponse('html/store.html')

@app.get('/tools')
def tools():
    return FileResponse('html/tools.html')

@app.get('/history')
def history():
    return FileResponse('html/history.html')

@app.get('/contact')
def contact():
    return FileResponse('html/contact.html')

@app.get('/register')
def contact():
    return FileResponse('html/register.html')