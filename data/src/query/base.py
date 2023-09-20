"""Base
"""

from query.spec import QuerySpec, Specs


class Query:
    """A class for creating basic queries."""

    def __init__(self, columns="", tables="", constraints="", spec=Specs.DEFAULT):
        """_summary_

        Args:
            columns (str, optional): The list of columns. Defaults to "*".
            tables (str, optional): The list of tables. Defaults to "".
            constraints (str, optional): The query constraints. Defaults to "".
        """
        self._query_string = self.construct(
            columns, tables, constraints, Specs.default_spec()
        )

    def __str__(self):
        return self._query_string.format()

    def __format__(self, format_spec):
        return format(self._query_string, format_spec)

    def construct(self, columns, tables, constraints, spec: QuerySpec) -> str:
        """Constructs the query string.

        Args:
            columns (_type_): _description_
            tables (_type_): _description_
            constraints (_type_): _description_

        Returns:
            str: _description_
        """
        _select = f"{spec['select_spec']} {columns}"
        _from = f"{spec['from_spec']} {tables}"
        _where = f"{spec['where_spec']} {constraints}"
        return f"{_select}{_from}{_where}"
