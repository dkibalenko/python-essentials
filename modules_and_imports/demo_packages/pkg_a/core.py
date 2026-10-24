"""Core objects for pkg_a."""
from __future__ import annotations

print("[pkg_a.core] loading")


class Counter:
    """Simple counter — used throughout module system demos."""

    def __init__(self, start: int = 0) -> None:
        self._value = start

    def increment(self) -> None:
        self._value += 1

    @property
    def value(self) -> int:
        return self._value

    def __repr__(self) -> str:
        return f"Counter({self._value})"


def greet(name: str) -> str:
    return f"Hello, {name}!"
