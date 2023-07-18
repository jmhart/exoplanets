from src.etl.query.base import Query


def test_base_query_returns_string():
    query = Query()
    result = str(query)
    assert isinstance(result, str)
