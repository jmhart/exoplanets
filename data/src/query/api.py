import requests

from query.nasa import NasaQuery


def getPlanets(nasa_query: NasaQuery):
    base = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query="
    url = f"{base}{str(nasa_query)}"
    response = requests.get(url, timeout=5000)
    return response.json()
