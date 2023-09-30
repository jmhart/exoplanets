from query.nasa import NasaQuery


def xtest_get_planets():
    nasa_query = NasaQuery("*", "ps", "pl_rade+<+=+1.8+and+pl_masse+>+0")
    result = ""

    assert result is not None
    assert len(result) > 0
