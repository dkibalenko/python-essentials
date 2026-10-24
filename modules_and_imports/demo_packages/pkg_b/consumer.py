"""
pkg_b consuming from pkg_a — cross-package import demo.

Key point: when this module is imported, pkg_a.__init__.py does NOT
re-execute. Python finds 'pkg_a' already in sys.modules and returns
the cached module object. The [pkg_a.__init__] print will only
appear once per kernel session, no matter how many modules import it.
"""
from __future__ import annotations

print("[pkg_b.consumer] loading")

from pkg_a import greet          # uses pkg_a's __init__ public API
from pkg_a.utils import shout    # goes directly to the submodule


def welcome(name: str) -> str:
    return shout(name)
