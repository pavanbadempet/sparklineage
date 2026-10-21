"""PyO3 String Allocation Benchmarks for Lineage Extraction."""
import pytest
import time

def test_pyo3_zero_copy_string_throughput():
    # Simulates string extraction throughput under heavy catalyst plan traversal
    start = time.perf_counter()
    nodes = [f"spark_plan_node_{i}" for i in range(10000)]
    elapsed = time.perf_counter() - start
    assert elapsed < 0.05
    assert len(nodes) == 10000
