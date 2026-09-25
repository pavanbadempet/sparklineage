"""
Subquery alias resolution module for deeply nested Spark SQL projections.
"""
from typing import Dict, List, Optional

class SubqueryAliasResolver:
    """Resolves subquery aliases to prevent lineage shadowing in nested SQL expressions."""

    def __init__(self) -> None:
        self._alias_registry: Dict[str, str] = {}

    def register_alias(self, alias_name: str, target_table: str) -> None:
        self._alias_registry[alias_name] = target_table

    def resolve(self, column_ref: str) -> str:
        if "." in column_ref:
            alias, col = column_ref.split(".", 1)
            target = self._alias_registry.get(alias, alias)
            return f"{target}.{col}"
        return column_ref
