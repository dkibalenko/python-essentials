"""
FIXED circular import — deferred import pattern.

The import is moved INSIDE the function body.
It runs when func_a() is CALLED, not when this module loads.
By call time, both modules are fully initialized and both have
all their names defined.
"""
print("[fixed_a] loading — no import of fixed_b happens yet")


def func_a() -> str:
    from circular_demo.fixed_b import func_b   # ← deferred: runs at call time
    return f"func_a got: '{func_b()}'"
