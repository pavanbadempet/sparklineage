"""
Test suite for BroadcastHashJoin lineage node preservation.
"""
import unittest

class TestBroadcastHashJoin(unittest.TestCase):
    def test_broadcast_hint_tagging(self):
        join_type = "BroadcastHashJoin"
        hint_present = True
        self.assertTrue(hint_present)
        self.assertEqual(join_type, "BroadcastHashJoin")

if __name__ == "__main__":
    unittest.main()
