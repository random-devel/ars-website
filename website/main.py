from fastapi import FastAPI, Depends, status, Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import sqlite3
from passgen import generate

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

@app.post('/login')
def cred(username : str = Form(...), password : str = Form(...)):
    return {'null':'null'}





@app.get('/register')
def contact():
    return FileResponse('html/register.html')

@app.post('/register')
def reg(email : str = Form(...)):
    return {'hello':'hello'}


@app.get('/register/passwd')
def make_passwd():
    pass


@app.get('/passwd')
def passwd():
    return FileResponse('html/pass.html')


@app.get('/profile')
def profile():
    return FileResponse('html/profile.html')

@app.get('/services')
def sotre():
    return FileResponse('html/services.html')

@app.get('/tools')
def tools():
    return FileResponse('html/tools.html')

@app.get('/history')
def history():
    return FileResponse('html/history.html')

