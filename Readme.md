This will be a small full stack project. Here we will be building simple user login page via calling frontend and backend. 

Frontend: Login page where user enters username and password
Backend: FastAPI server that receives username/password and checks login logic

For this simple version, we will not use a database yet.

Frontend:
-Taking username input
-Taking password input
-Calling backend API when Login button is clicked
-Showing success/error message

Backend:
-Receiving username and password
-Validating request data
-Checking whether username/password are correct
-Returning success or failure response


COMMUNICATION:

        User enters username/password
                        ↓
        User clicks Login button
                        ↓
        Frontend sends POST request to FastAPI backend
                        ↓
        FastAPI checks login details
                        ↓
        FastAPI sends response back
                        ↓
        Frontend displays success or error message


BACKEND LIBRARIES:
-FastAPI: For building the backend API
-uvicorn: For running the FastAPI server
-pydantic: For data validation

FRONTEND LIBRARIES:
  Basic one: HTML/CSS/JavaScript
    Optional: React or Vue.js for better UI/UX (not required for this simple version


backend/main.py         -> FastAPI backend code
backend/requirements.txt -> Python dependencies
frontend/index.html     -> Login page structure
frontend/style.css      -> Login page design
frontend/script.js      -> Logic to call backend API
