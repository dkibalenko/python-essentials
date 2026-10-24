"""module_ref_b — imported by module_ref_a as a module object (not symbol)."""
print("[module_ref_b] loading")


def func_b() -> str:
    return "module_ref_b result"
