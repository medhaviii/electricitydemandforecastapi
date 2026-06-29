from pydantic import BaseModel

class PredictionRequest(BaseModel):
    state: str
    datetime: str