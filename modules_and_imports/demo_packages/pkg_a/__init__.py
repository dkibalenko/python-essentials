"""
pkg_a — sample package for module system exploration.

This __init__.py runs ONCE when pkg_a is first imported.
Every subsequent import — from any file in the process — finds
the already-initialised object in sys.modules and skips this file.
"""
print(f"[pkg_a.__init__] initializing  (id={id(__name__)})")

from pkg_a.core import Counter, greet  # expose at package level

__all__ = ["Counter", "greet", "utils", "sub"]
