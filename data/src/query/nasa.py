"""Nasa query"""


from query.base import Query


class NasaQuery(Query):
    """A class to create NASA exoplanet database queries. All queries must
    have valid ADQL, which takes the form:

    SELECT <column list> FROM <table> WHERE <constraints>

    For more information, visit this link:
    https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html
    """

    def __init__(self, columns: str, tables: str, constraints: str):
        super(NasaQuery, self).__init__(columns, tables, constraints)

    def construct(self, columns: str, tables: str, constraints: str) -> str:
        """all spaces in the SQL should be replaced with a plus (+) symbol."""
        _select = f"select+{columns.replace(' ', '+')}"
        _from = f"+from+{tables.replace(' ', '+')}"
        _where = f"+where+{constraints.replace(' ', '+')}"
        return f"{_select}{_from}{_where}&format=json"
