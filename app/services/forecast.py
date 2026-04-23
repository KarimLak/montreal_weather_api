from app.schemas.forecast import ForecastCreateDaily, ForecastCreateWeekly, ForecastResponseDaily, ForecastResponseWeekly
import openmeteo_requests

class ForecastService:
    def __init__(self):
        self.url = "https://api.open-meteo.com/v1/forecast"
        self.openmeteo = openmeteo_requests.Client()

    def get_forecast_daily(self, payload: ForecastCreateDaily) -> ForecastResponseDaily:
        responses = self.openmeteo.weather_api(self.url, params = payload.model_dump())
        min_value = responses[0].Daily().Variables(0).ValuesAsNumpy().tolist()
        max_value = responses[0].Daily().Variables(1).ValuesAsNumpy().tolist()
        return ForecastResponseDaily(
            min_temperature = min_value[0],
            max_temperature = max_value[0]
        )
    
    def get_forecast_weekly(self, payload: ForecastCreateWeekly) -> ForecastResponseWeekly:
        responses = self.openmeteo.weather_api(self.url, params = payload.model_dump())
        min_value = responses[0].Daily().Variables(0).ValuesAsNumpy().tolist()
        max_value = responses[0].Daily().Variables(1).ValuesAsNumpy().tolist()
        return ForecastResponseWeekly(
            min_temperature = min_value,
            max_temperature = max_value
        )
        
def get_forecast_service() -> ForecastService:
    return ForecastService()
    



