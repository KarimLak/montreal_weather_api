from app.schemas.forecast import ForecastCreateDaily, ForecastCreateWeekly, ForecasteResponse
import openmeteo_requests

class ForecastService:
    def __init__(self):
        self.url = "https://api.open-meteo.com/v1/forecast"
        self.openmeteo = openmeteo_requests.Client()

    def get_forecast_daily(self, payload: ForecastCreateDaily) -> ForecasteResponse:
        responses = self.openmeteo.weather_api(self.url, params = payload.model_dump())
        min_value = responses[0].Daily().Variables(0).ValuesAsNumpy().tolist()
        max_value = responses[0].Daily().Variables(1).ValuesAsNumpy().tolist()
        return ForecasteResponse(
            min_temperature = min_value[0],
            max_temperature = max_value[0]
        )
    
    def get_forecast_weekly(self, payload: ForecastCreateWeekly):
        responses = self.openmeteo.weather_api(self.url, params = payload)
        return  responses[0]
        
def get_forecast_service() -> ForecastService:
    return ForecastService()
    



