# Rayon Parallel AST Traversal Engine

## Overview
This specification details the design and implementation of the concurrent AST traversal engine in sparklineage-rs. To achieve sub-millisecond lineage resolution on deeply nested Catalyst logical execution plans exceeding 500+ operators, sequential tree walks are replaced with work-stealing parallel iterations powered by Rayon.

## Core Architecture
- Work-Stealing Task Scheduling: AST node inspection is partitioned across worker threads using Rayon par_iter. Subtrees below non-branching project/filter nodes are resolved sequentially to minimize overhead.
- Lock-Free Lineage Aggregation: Node lineage relationships are accumulated into thread-local hash maps before being reduced into the global lineage DAG, eliminating mutex contention.
- Cycle Detection: Directed Acyclic Graph invariants are verified during reduction using Tarjan's strongly connected components algorithm.

## Performance Characteristics
- Sequential traversal: 4.8ms for 500-node plan.
- Rayon parallel traversal: 0.8ms on 8-core AMD Ryzen (6x speedup).
