# SPIP Security Controls: Data Lineage Credential Masking

## Objective
Prevent accidental credential exposure in serialized Spark execution plans.

## Masking Rules
1. Pre-commit AST inspection for hardcoded SAS tokens, AWS session keys, and JDBC passwords.
2. In-memory redaction before Mermaid DAG rendering.
3. Strict environment variable validation for cloud lakehouse endpoints.
