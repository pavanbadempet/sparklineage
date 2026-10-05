# Delta Lake Change Data Feed (CDF) Lineage Extraction

## Abstract
Delta Lake table versions store row-level mutations via Change Data Feed. This document outlines how sparklineage extracts schema mutations and change event dependencies directly from Delta commit logs without scanning full underlying Parquet files.

## Metadata Inspection
- Read Delta transaction log _delta_log/*.json using lightweight JSON stream parser.
- Identify add and remove actions to map column-level changes between table commits.
- Link versioned commit snapshots to Spark job IDs for point-in-time auditing.
