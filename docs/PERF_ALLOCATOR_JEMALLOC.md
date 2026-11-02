# Memory Allocator Profiling: jemalloc in Rust Core

## Background
Standard glibc malloc exhibits heap fragmentation under high-frequency short-lived string allocations.
Using `jemalloc` on Linux x86_64 reduces peak RSS by up to 28% during large workspace lineage scans.
