import sys

from etl import app


def main() -> str:
    """Package entry point.

    Returns:
        str: A status message.
    """
    try:
        return app.start()
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    sys.exit(main())
