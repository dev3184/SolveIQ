import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from apps.calculator.route import router as calculator_router
from constants import SERVER_URL, PORT, ENV

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

# CORS Configuration - Allow only frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allow frontend only
    allow_credentials=True,
    allow_methods=["*"],  # Explicit allowed methods
    allow_headers=["*"],  # Allow all headers
)

@app.get('/')
async def root():
    return {"message": "Server is running"}

# Include Calculator Router
app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])

if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_URL, port=int(PORT), reload=(ENV == "dev"))
