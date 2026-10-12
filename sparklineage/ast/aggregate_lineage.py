"""
Lineage tracking through multi-dimensional aggregation operations (Rollup, Cube, Grouping Sets).
"""
from typing import List, Set

class AggregateLineageTracker:
    """Extracts input-to-output dependencies for complex aggregation groupings."""

    @staticmethod
    def extract_grouping_columns(grouping_expressions: List[str]) -> Set[str]:
        columns = set()
        for expr in grouping_expressions:
            cleaned = expr.strip().replace("`", "")
            columns.add(cleaned)
        return columns
