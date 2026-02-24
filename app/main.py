
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import auth, doctors, appointments, medicines, ai_chat

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Healthify API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(doctors.router)
app.include_router(appointments.router)
app.include_router(medicines.router)
app.include_router(ai_chat.router)

@app.get("/")
def root():
    return {"message": "Healthify Backend Running"}
