"""app.py
"""


def start(options="*") -> str:
    """Starts the application.

    Returns:
        str: A status message.
    """
    match options:
        case "planets":
            result = 0
            return f"Planets ETL job completed in {result} seconds"
        case _:
            return "Default"
