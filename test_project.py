from project import air_quality, get_city_lat_long, current_weather
import pytest


def main():
  test_get_city_lat_long()
  test_air_quality()
  test_current_weather()


def test_get_city_lat_long():
  assert get_city_lat_long('pune') == (
      18.521428, 73.8544541, "IN", "Maharashtra", "Pune")
  assert get_city_lat_long('lonDon') == (
      51.5073219, -0.1276474, "GB", "England", "London")
  assert get_city_lat_long('New York') == (
      40.7127281, -74.0060152, "US", "New York", "New York County")
  assert get_city_lat_long('Delhi') == (
      28.6517178, 77.2219388, "IN", "Delhi", "Delhi")



@pytest.mark.parametrize('city, tuple_data', [
    ('pune', (18.521428, 73.8544541, "IN", "Maharashtra", "Pune")),
    ('lonDon', (51.5073219, -0.1276474, "GB", "England", "London")),
    ('New York', (40.7127281, -74.0060152, "US", "New York", "New York County")),
    ('Delhi  ', (28.6517178, 77.2219388, "IN", "Delhi", "Delhi")),
  ], ids=["Pune", "London", "New York", "Delhi"])
def test_get_city_lat_long(city, tuple_data):
  assert get_city_lat_long(city) == tuple_data


def test_air_quality():
  assert air_quality("sbjsbhjbjd") == ("", "")


def test_current_weather():
  assert current_weather('svnbdvngdenb as') == "\n City not found ❌; Please, enter correct city name!"



if __name__ == "__main__":
  main()
