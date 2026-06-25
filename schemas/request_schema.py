from pydantic import BaseModel


class PredictionRequest(BaseModel):
    datetime: str