from fastapi import FastAPI
from router.weather import weather_router

app = FastAPI()

app.include_router(weather_router)

