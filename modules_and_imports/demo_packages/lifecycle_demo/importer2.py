"""
Second module that imports once.py.
When imported AFTER importer1, once.py is already in sys.modules —
its init print does NOT appear again, but _call_count continues incrementing.
"""
print("[importer2] loading, importing once...")
from lifecycle_demo.once import get_count
print(f"[importer2] done. get_count() = {get_count()}")
