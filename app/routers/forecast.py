from fastapi import APIRouter, Depends, FastAPI

from app.schemas.forecast import ForecastCreateDaily, ForecastCreateWeekly, ForecastResponseDaily, ForecastResponseWeekly
from app.services.forecast import ForecastService, get_forecast_service

forecast_router = APIRouter()

@forecast_router.post('/forecast/daily', response_model=ForecastResponseDaily)
def get_forecast(payload: ForecastCreateDaily, service: ForecastService = Depends(get_forecast_service)):
    return service.get_forecast_daily(payload)

@forecast_router.post('/forecast/weekly', response_model=ForecastResponseWeekly)
def get_forecast(payload: ForecastCreateWeekly, service: ForecastService = Depends(get_forecast_service)):
    return service.get_forecast_weekly(payload)







