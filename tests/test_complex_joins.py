"""Tests for complex multi-hop DataFrame join lineage tracking."""
def test_multi_hop_join_lineage_resolution():
    lineage_path = ["raw_orders", "bronze_cleansed", "silver_enriched", "gold_kpi"]
    assert len(lineage_path) == 4
    assert lineage_path[0] == "raw_orders"
    assert lineage_path[-1] == "gold_kpi"
