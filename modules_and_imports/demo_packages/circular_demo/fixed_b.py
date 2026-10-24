"""FIXED circular import — other half. No import of fixed_a at module level."""
print("[fixed_b] loading")


def func_b() -> str:
    return "fixed_b result"
