from app.schemas.forecast import ForecasteResponse

class ForecastService:
    def get_forecast(payload) -> ForecasteResponse:
        return 0
        
def get_forecast_service() -> ForecastService:
    return ForecastService()
    



