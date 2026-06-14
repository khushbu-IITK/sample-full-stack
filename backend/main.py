from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


# Create FastAPI app
app = FastAPI()


# Allow frontend to call backend
# This is needed because frontend and backend run on different ports.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For learning only. In production, use exact frontend URL.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define what data we expect from frontend
class LoginRequest(BaseModel):
    username: str
    password: str


# Simple test user
# Later this can come from database
VALID_USERNAME = "admin"
VALID_PASSWORD = "admin123"


@app.get("/")
def home():
    return {
        "message": "FastAPI backend is running"
    }


@app.post("/login")
def login(user: LoginRequest):
    """
    This function handles login request.
    It receives username and password from frontend.
    """

    if user.username == VALID_USERNAME and user.password == VALID_PASSWORD:
        return {
            "success": True,
            "message": "Login successful"
        }

    return {
        "success": False,
        "message": "Invalid username or password"
    }