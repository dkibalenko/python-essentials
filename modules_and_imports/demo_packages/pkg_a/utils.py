"""
Utility helpers — demonstrates intra-package imports.

Both absolute and relative import forms are shown as comments.
Either works; relative is more portable (survives package renames).
"""
from __future__ import annotations

print("[pkg_a.utils] loading")

from pkg_a.core import greet      # absolute intra-package import
# from .core import greet         # relative equivalent — identical result


def shout(name: str) -> str:
    return greet(name).upper()
