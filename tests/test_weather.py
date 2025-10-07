from src.weather import WeatherReading, WeatherModel
import math

def test_average_temp():
    m = WeatherModel([WeatherReading('t1', 20, 0, 0), WeatherReading('t2', 22, 0, 0)])
    assert abs(m.average_temp() - 21) < 1e-9

def test_max_wind():
    m = WeatherModel([])
    assert math.isnan(m.max_wind())
