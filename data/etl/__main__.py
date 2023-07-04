"""__main__.py
"""
import sys

from etl import app


def main() -> str:
    """Package entry point.

    Returns:
        str: A status message.
    """
    try:
        return app.start()
    except ValueError as value_error:
        return str(value_error)


if __name__ == "__main__":
    sys.exit(main())
