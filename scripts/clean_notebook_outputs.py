#!/usr/bin/env python3
"""Strip outputs and execution counters from Jupyter notebooks."""

import json
import sys
from pathlib import Path


def clean_notebook(path: Path) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = False

    for cell in data.get("cells", []):
        if cell.get("cell_type") != "code":
            continue

        if cell.get("outputs"):
            cell["outputs"] = []
            changed = True

        if cell.get("execution_count") is not None:
            cell["execution_count"] = None
            changed = True

    if changed:
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )

    return changed


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: clean_notebook_outputs.py <notebook-path> [<notebook-path> ...]")
        return 1

    changed_files = []
    for raw in sys.argv[1:]:
        notebook_path = Path(raw)
        if not notebook_path.exists() or notebook_path.suffix != ".ipynb":
            continue

        if clean_notebook(notebook_path):
            changed_files.append(str(notebook_path))

    if changed_files:
        print("Cleaned notebook outputs:")
        for item in changed_files:
            print(f"- {item}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
