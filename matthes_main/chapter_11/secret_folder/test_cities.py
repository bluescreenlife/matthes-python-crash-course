from city_functions import city_country

def test_city_country_population():
    location = city_country("minneapolis", "united states", 500000)
    assert location == "Minneapolis, United States - population = 500000"

def test_city_country():
    location = city_country("minneapolis", "united states")
    assert location == "Minneapolis, United States"