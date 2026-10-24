"""
WORKS — importing the module object, not a symbol.

'import circular_demo.module_ref_b' works even in a circular scenario
because Python only needs the module OBJECT to exist in sys.modules —
not for specific names to be defined on it yet.

The attribute access mod_b.func_b() is resolved at CALL TIME, not at
import time, so by then module_ref_b is fully initialized.
"""
print("[module_ref_a] loading")

import circular_demo.module_ref_b as mod_b   # import module — works even if b imports a


def func_a() -> str:
    return f"module_ref_a.func_a → calls mod_b.func_b: '{mod_b.func_b()}'"
