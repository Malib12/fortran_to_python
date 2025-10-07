from .weather import WeatherReading, WeatherModel
from pathlib import Path

def load_from_csv(path):
    readings = []
    with open(path) as f:
        next(f)
        for line in f:
            ts, t, h, w = line.strip().split(',')
            readings.append(WeatherReading(ts, float(t), float(h), float(w)))
    return readings

if __name__ == "__main__":
    readings = load_from_csv(Path("data/weather_sample.csv"))
    model = WeatherModel(readings)
    print("Avg temp:", model.average_temp())
    print("Max wind:", model.max_wind())
    print("Class:", model.classify_day())
