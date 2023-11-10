from api.exoplanets import get
from query.nasa import NasaQuery


def test_get_planets():
    nasa_query = NasaQuery("*", "ps", "pl_masse between 0.5 and 2.0")
    result = get(nasa_query)

    first = result[0]

    assert result is not None
    assert len(result) > 0
