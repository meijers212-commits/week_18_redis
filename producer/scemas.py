from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Alerts(BaseModel):
    border: str
    zone: str
    timestamp: datetime
    people_count: int
    weapons_count: int
    vehicle_type: str
    distance_from_fence_m: int
    visibility_quality: float
