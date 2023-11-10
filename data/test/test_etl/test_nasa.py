from query.nasa import NasaQuery


def test_nasa_query_constructs():
    nasa_query = NasaQuery("*", "ps", "pl_rade < = 1.8 and pl_masse > 0")
    expected = "select+*+from+ps+where+pl_rade+<+=+1.8+and+pl_masse+>+0&format=json"

    assert str(nasa_query) == expected
