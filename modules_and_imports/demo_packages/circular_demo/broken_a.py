"""
BROKEN circular import — will raise ImportError.

What happens when Python imports this module:
  1. Python pre-registers 'circular_demo.broken_a' in sys.modules (empty stub)
  2. Starts executing broken_a.py
  3. Hits: from circular_demo.broken_b import func_b
  4. Starts importing broken_b
  5. broken_b hits: from circular_demo.broken_a import func_a
  6. broken_a IS in sys.modules — but it's still the EMPTY stub from step 1
  7. func_a doesn't exist on that stub yet → ImportError: cannot import name 'func_a'

DO NOT import this module directly. Use the notebook's try/except demo.
"""
print("[broken_a] loading")

from circular_demo.broken_b import func_b   # ← triggers broken_b load


def func_a() -> str:
    return "func_a result"
