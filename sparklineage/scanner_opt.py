"""Optimized regex compilation for Rayon parallel scanner."""
import re

CREDENTIAL_PATTERNS = [
    re.compile(r'(?i)password\s*[:=]\s*["'][^"']+["']'),
    re.compile(r'(?i)secret\s*[:=]\s*["'][^"']+["']'),
    re.compile(r'(?i)token\s*[:=]\s*["'][^"']+["']'),
]

def scan_text_safe(text: str) -> bool:
    return any(p.search(text) for p in CREDENTIAL_PATTERNS)
