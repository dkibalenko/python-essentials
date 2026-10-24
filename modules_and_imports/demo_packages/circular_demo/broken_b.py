"""BROKEN circular import — the other half."""
print("[broken_b] loading")

from circular_demo.broken_a import func_a   # ← broken_a stub has no func_a yet!


def func_b() -> str:
    return "func_b result"
