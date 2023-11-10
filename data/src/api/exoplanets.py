"""http"""

import requests

from query.nasa import NasaQuery


def get(nasa_query: NasaQuery):
    """Gets exoplanet data from NASA archive.

    Args:
        nasa_query (NasaQuery): The NASA query argument.

    Returns:
        _type_: _description_
    """
    base = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query="
    url = f"{base}{str(nasa_query)}"
    response = requests.get(url, timeout=5000)
    return response.json()
