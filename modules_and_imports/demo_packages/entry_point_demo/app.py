"""app.py — runnable as a script AND importable as a module.

Used to demonstrate that the entry-point script and an import of
the same file by its real module name are two independent
executions, cached under two different sys.modules keys.
"""

print(f"[app.py] module-level code executing — __name__ = {__name__!r}")


def main() -> None:
    print("[app.py] main() running — entry-point-only logic")


if __name__ == "__main__":
    main()
