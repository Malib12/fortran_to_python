from dataclasses import dataclass
import numpy as np
import math

@dataclass
class WeatherReading:
    timestamp: str
    temp_c: float
    humidity: float
    wind_mps: float

class WeatherModel:
    def __init__(self, readings=None):
        self.readings = readings or []

    def average_temp(self):
        arr = np.array([r.temp_c for r in self.readings], dtype=float)
        return float(arr.mean()) if arr.size else math.nan

    def max_wind(self):
        arr = np.array([r.wind_mps for r in self.readings], dtype=float)
        return float(arr.max()) if arr.size else math.nan

    def classify_day(self):
        avg = self.average_temp()
        if math.isnan(avg):
            return "NO_DATA"
        elif avg >= 30: return "HOT"
        elif avg >= 20: return "MILD"
        else: return "COOL"
