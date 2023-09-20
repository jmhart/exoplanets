"""QuerySpec
"""
from enum import Enum
from typing import TypedDict


class QuerySpec(TypedDict):
    """A class representing a query's specification."""

    select_spec: str
    from_spec: str
    where_spec: str


class Specs(Enum):
    """An enum containing Spec strings and static methods."""

    DEFAULT = "Default"

    @staticmethod
    def default_spec() -> QuerySpec:
        """Returns the default QuerySpec.

        Returns:
            QuerySpec: A class representing a query's specification.
        """
        spec: QuerySpec = {
            "select_spec": "select",
            "from_spec": "from",
            "where_spec": "where",
        }

        return spec
