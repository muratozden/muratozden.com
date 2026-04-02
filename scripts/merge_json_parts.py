#!/usr/bin/env python3
"""Merge *.partNNN.json back into a single {stem}.json (for re-splitting)."""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


PART_RE = re.compile(r"^(.+)\.part(\d+)\.json$", re.IGNORECASE)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", type=Path, default=Path(__file__).resolve().parent.parent / "data")
    args = ap.parse_args()
    data_dir: Path = args.data_dir

    groups: dict[str, list[tuple[int, Path]]] = defaultdict(list)
    for p in data_dir.glob("*.json"):
        if p.name == "manifest.json":
            continue
        m = PART_RE.match(p.name)
        if m:
            groups[m.group(1)].append((int(m.group(2)), p))

    for stem, items in sorted(groups.items()):
        items.sort(key=lambda x: x[0])
        paths = [p for _, p in items]
        meta = None
        merged: list = []
        for p in paths:
            doc = json.loads(p.read_text(encoding="utf-8"))
            if meta is None:
                meta = {k: doc[k] for k in ("generatedAt", "source", "total", "successCount") if k in doc}
            merged.extend(doc.get("data") or [])
        out_path = data_dir / f"{stem}.json"
        if out_path.exists():
            raise SystemExit(f"refuse overwrite: {out_path}")
        out_doc = {**meta, "data": merged}
        out_path.write_text(
            json.dumps(out_doc, ensure_ascii=False, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
        for p in paths:
            p.unlink()
        print(f"merged {stem} <- {len(paths)} parts, {len(merged)} rows -> {out_path.name}")


if __name__ == "__main__":
    main()
