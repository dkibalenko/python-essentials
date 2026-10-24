"""
This module prints when it loads.
No matter how many files import it, this print runs EXACTLY ONCE per process.
After the first import, sys.modules['lifecycle_demo.once'] returns the
cached module object — this file is never executed again.

Consequence: _call_count is shared state across ALL importers.
"""
print("[lifecycle_demo.once] ← this prints ONCE, no matter how many importers exist")

_call_count = 0


def get_count() -> int:
    """Each call increments a counter shared across the entire process."""
    global _call_count
    _call_count += 1
    return _call_count
