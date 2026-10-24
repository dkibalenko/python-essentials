"""
Demonstrates relative import from inside a subpackage.

  from ..core import Counter
  │
  ├── ..   → go up one level: pkg_a.sub → pkg_a
  └── core → then enter the core module

Relative imports require __package__ to be set, which happens
automatically when this file is part of a package.
"""
from __future__ import annotations

print("[pkg_a.sub.helper] loading")

from pkg_a.core import Counter      # absolute form
# from ..core import Counter        # relative equivalent


def make_counter(start: int = 0) -> Counter:
    return Counter(start)
