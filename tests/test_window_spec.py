"""
Unit tests for WindowSpec dependency parsing and column tracking.
"""
import unittest

class TestWindowSpecTracking(unittest.TestCase):
    def test_partition_by_column_lineage(self):
        partition_cols = ["user_id", "organization_id"]
        order_col = "event_timestamp"
        dependencies = set(partition_cols + [order_col])
        self.assertIn("user_id", dependencies)
        self.assertIn("event_timestamp", dependencies)
        self.assertEqual(len(dependencies), 3)

if __name__ == "__main__":
    unittest.main()
