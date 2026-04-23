from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field

class ForecastCreate(BaseModel):
    latitude: float = Field(45.5017, ge=-90, le=90)
    longitude: float = Field(-73.5673, ge=-180, le=180)

class ForecastCreateDaily(ForecastCreate):
    daily: List[str] = ["temperature_2m_min", "temperature_2m_max"]
    past_days: int = 0
    forecast_days: int = 1
    timezone: str = "auto"

class ForecastCreateWeekly(ForecastCreate):
    daily: List[str] = ["temperature_2m_min", "temperature_2m_max"]
    past_days: int = 0
    forecast_days: int = 7
    timezone: str = "auto"

class ForecastResponseDaily(BaseModel):
    min_temperature: float = Field(...)
    max_temperature: float = Field(...)

class ForecastResponseWeekly(BaseModel):
    min_temperature: List[float] = Field(...)
    max_temperature: List[float] = Field(...)

