from query.api import get_planets
from query.nasa import NasaQuery


def test_get_planets():
    nasa_query = NasaQuery("*", "ps", "pl_rade+<+=+1.8+and+pl_masse+>+0")
    result = get_planets(nasa_query)

    assert result is not None
    assert len(result) > 0
