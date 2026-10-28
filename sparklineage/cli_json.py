"""JSON output formatter for CI/CD pipeline integration."""
import json
from typing import Dict, Any

def format_lineage_json(dag_metadata: Dict[str, Any]) -> str:
    return json.dumps({
        "status": "success",
        "nodes_count": len(dag_metadata.get("nodes", [])),
        "edges_count": len(dag_metadata.get("edges", [])),
        "hazards": dag_metadata.get("hazards", []),
    }, indent=2)
