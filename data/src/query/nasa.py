"""Nasa query"""


from query.base import Query
from query.spec import QuerySpec


class NasaQuery(Query):
    """A class to create NASA exoplanet database queries. All queries must
    have valid ADQL, which takes the form:

    SELECT <column list> FROM <table> WHERE <constraints>

    For more information, visit this link:
    https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html
    """

    def __init__(self, columns, tables, constraints):
        super(NasaQuery, self).__init__(columns, tables, constraints)

    def construct(self, columns, tables, constraints, spec: QuerySpec = None) -> str:
        """all spaces in the SQL should be replaced with a plus (+) symbol."""
        _select = f"select+{columns}"
        _from = f"+from+{tables}"
        _where = f"+where+{constraints}"
        return f"{_select}{_from}{_where}&format=json"
