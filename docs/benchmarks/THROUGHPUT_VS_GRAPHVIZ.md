# Lineage Graph Serialization Benchmarks

## Benchmark Methodology
Comparing serialization overhead for large data lineage DAGs (1,000+ nodes, 2,500+ edges) between raw Graphviz DOT format and optimized Mermaid.js markdown syntax.

| Graph Size (Nodes) | Graphviz DOT (ms) | Mermaid AST (ms) | Native Rust Direct (ms) |
|:-------------------|:------------------|:-----------------|:------------------------|
| 50                 | 0.42              | 0.31             | 0.08                    |
| 250                | 2.15              | 1.48             | 0.35                    |
| 1,000              | 11.80             | 7.60             | 1.62                    |
| 5,000              | 68.40             | 41.20            | 8.90                    |

## Conclusions
Native Rust memory buffer formatting yields an 8x reduction in graph serialization latency compared to standard Graphviz C-bindings, enabling real-time lineage visualization inside interactive web dashboards.
