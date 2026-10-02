"""
OpenLineage JSON format exporter for Spark lineage metadata.
"""
import json
from typing import Any, Dict, List

class OpenLineageFormatter:
    """Formats lineage graphs into OpenLineage standard JSON event structures."""

    def __init__(self, job_name: str, namespace: str = "default") -> None:
        self.job_name = job_name
        self.namespace = namespace

    def format_run_event(self, inputs: List[str], outputs: List[str]) -> Dict[str, Any]:
        return {
            "eventType": "COMPLETE",
            "job": {"namespace": self.namespace, "name": self.job_name},
            "inputs": [{"namespace": self.namespace, "name": inp} for inp in inputs],
            "outputs": [{"namespace": self.namespace, "name": out} for out in outputs]
        }
