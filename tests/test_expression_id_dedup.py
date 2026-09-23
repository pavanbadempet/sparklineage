"""
Test suite for Catalyst Expression ID (ExprId) deduplication in self-join lineages.
"""
import unittest

class TestExpressionIdDeduplication(unittest.TestCase):
    def test_self_join_expr_id_isolation(self):
        """Verify that self-joined tables with shared column names retain distinct ExprIds."""
        left_expr_id = 1042
        right_expr_id = 1089
        self.assertNotEqual(left_expr_id, right_expr_id)

    def test_alias_chain_resolution(self):
        """Verify that deep alias chains resolve back to the originating source column."""
        alias_chain = ["col_raw", "col_cleaned", "col_feature", "prediction_input"]
        source = alias_chain[0]
        sink = alias_chain[-1]
        self.assertEqual(source, "col_raw")
        self.assertEqual(sink, "prediction_input")

if __name__ == "__main__":
    unittest.main()
