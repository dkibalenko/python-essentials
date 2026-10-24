"""
First module that imports once.py.
When imported, this triggers lifecycle_demo.once to initialize.
"""
print("[importer1] loading, importing once...")
from lifecycle_demo.once import get_count
print(f"[importer1] done. get_count() = {get_count()}")
