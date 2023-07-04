"""Test etl.app
"""


from src.etl import app


def test_app_start():
    result = app.start()
    assert isinstance(result, str)
