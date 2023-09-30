"""Base"""

from query.spec import QuerySpec, Specs


class Query:
    """A base class for creating queries."""

    def __init__(self, columns="", tables="", constraints=""):
        """
        Args:
            columns (str, optional): The list of columns. Defaults to "*".
            tables (str, optional): The list of tables. Defaults to "".
            constraints (str, optional): The query constraints. Defaults to "".
        """
        self._query_string = self.construct(columns, tables, constraints)

    def __str__(self):
        return self._query_string.format()

    def __format__(self, format_spec):
        return format(self._query_string, format_spec)

    def construct(self, columns, tables, constraints) -> str:
        """
        Constructs the query string.

        Args:
            columns (_type_): _description_
            tables (_type_): _description_
            constraints (_type_): _description_

        Returns:
            str: _description_
        """
        _select = f"select {columns}"
        _from = f"from {tables}"
        _where = f"where {constraints}"
        return f"{_select}{_from}{_where}"
