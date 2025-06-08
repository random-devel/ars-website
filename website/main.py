from fastapi import FastAPI, Form, Response, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException
from db_manange import db_auth, db_create_user, create_session, get_session, delete_session, fetch_user_data

#some feature will be added later
#like admin panel, user panel, etc.
#log the activities of the user
#log the activities of the admin
#log the activities of the system
#log the activities of the database
#log the activities of the server
#log the activities of the network
#log the activities of the hardware

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# get from the browser cookie the session_id
async def get_current_user(request: Request):
    """Helper function to get current user from session"""
    session_id = request.cookies.get("session_id")
    if not session_id:
        return None
    return get_session(session_id)

#exception handler for 404
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
async def cred(response: Response, username: str = Form(...), password: str = Form(...)):
    user = db_auth(username, password)
    if user:
        # Create session
        session_id = create_session(username)
        
        # Create response with redirect
        response = RedirectResponse(url="/profile", status_code=303)
        
        # Set session cookie
        response.set_cookie(
            key="session_id",
            value=session_id,
            httponly=True, # only the server can access the cookie
            max_age=3600,  # 1 hour
            path="/"
        )
        
        return response
    else:
        return {'error': 'Invalid credentials'}

@app.get('/register')
def register():
    return FileResponse('html/register.html')

@app.post('/register')
async def reg(username: str = Form(...), password: str = Form(...)):
    if db_create_user(username, password):
        create_session(username)
        return RedirectResponse(url="/profile", status_code=303)
    else:
        return {'error': 'user already exists'}

@app.get('/profile')
async def profile(request: Request):
    user = await get_current_user(request)
    if not user:
        return RedirectResponse(url="/login", status_code=303)
    return FileResponse('html/profile.html')

@app.get('/api/profile')
async def get_profile_data(request: Request):
    user = await get_current_user(request)
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {
        "username": user["username"],
        "login_time": user["created_at"],
        "email": fetch_user_data(user["username"])[1],
        "phone": fetch_user_data(user["username"])[2],
        "address": fetch_user_data(user["username"])[3],
        "city": fetch_user_data(user["username"])[4],
        "state": fetch_user_data(user["username"])[5],
        "zip": fetch_user_data(user["username"])[6]
    }

@app.get('/logout')
async def logout(request: Request):
    session_id = request.cookies.get("session_id")
    if session_id:
        delete_session(session_id)
    
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie(key="session_id")
    return response

@app.get('/services')
def store():
    return FileResponse('html/services.html')

@app.get('/tools')
def tools():
    return FileResponse('html/tools.html')

#we will discus this later caused by db not complete yet
@app.get('/api/tools')
def get_tools_data():
    return {
        "tools": [
            {
                "name": "Tool 1",
                "description": "Description 1",
                "price": 100
            }
        ]
    }


#we will discus this later caused by db not complete yet
@app.get('/api/services')
def get_services_data():
    return {
        "services": [
            {
                "name": "Service 1",
                "description": "Description 1",
                "price": 100
            }
        ]
    }

#we will discus this later caused by db not complete yet
@app.get('/api/training')
def get_training_data():
    return {
        "training": [
            {
                "name": "Training 1",
                "description": "Description 1",
                "price": 100
            }
        ]
    }


@app.get('/admin')
def admin():
    return FileResponse('html/admin.html')
