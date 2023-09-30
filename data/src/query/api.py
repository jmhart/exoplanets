"""api"""

import requests

from query.nasa import NasaQuery


def get_planets(nasa_query: NasaQuery):
    """_summary_

    Args:
        nasa_query (NasaQuery): _description_

    Returns:
        _type_: _description_
    """
    base = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query="
    url = f"{base}{str(nasa_query)}"
    response = requests.get(url, timeout=5000)
    return response.json()
