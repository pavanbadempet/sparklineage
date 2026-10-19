# Spark 3.5 Catalyst Compatibility Specification

## Overview
This document outlines the zero-copy PyO3 extraction layer for Apache Spark 3.5 logical plans.

### Key Plan Nodes Covered
- `ProjectExec` and `FilterExec` projection propagation.
- `ShuffledHashJoinExec` and `SortMergeJoinExec` join condition lineage tracking.
- `BroadcastNestedLoopJoinExec` hazard detection.

### Memory Overhead
- PyO3 reference borrows: 0 bytes heap allocation per parsed AST node.
- Sub-millisecond static extraction throughput across 1,000+ Catalyst operators.
