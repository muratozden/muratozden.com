#!/usr/bin/env python3
"""
Split epey-style JSON files in data/ when larger than --min-size.
Each output file keeps the same top-level metadata and a slice of `data`,
plus chunkIndex / chunkCount / splitStem.

Naming: {stem}.partNNN.json
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PART_RE = re.compile(r"^(.+)\.part(\d+)\.json$", re.IGNORECASE)


def is_part_file(name: str) -> bool:
    return PART_RE.match(name) is not None


def dumps_compact(obj) -> str:
    """Same as on-disk encoding (compact) so size limits match reality."""
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def json_bytes(obj) -> int:
    return len(dumps_compact(obj).encode("utf-8"))


def doc_size(meta: dict, stem: str, chunk_index: int, chunk_count: int, data: list) -> int:
    doc = {
        **meta,
        "chunkIndex": chunk_index,
        "chunkCount": chunk_count,
        "splitStem": stem,
        "data": data,
    }
    return json_bytes(doc)


def subdivide_until_under(
    chunk: list,
    meta: dict,
    stem: str,
    max_bytes: int,
    chunk_count_placeholder: int,
) -> list[list]:
    """Split item list until each piece serializes under max_bytes (best effort)."""
    if not chunk:
        return []
    size = doc_size(meta, stem, 1, chunk_count_placeholder, chunk)
    if size <= max_bytes or len(chunk) == 1:
        return [chunk]
    mid = max(1, len(chunk) // 2)
    return subdivide_until_under(
        chunk[:mid], meta, stem, max_bytes, chunk_count_placeholder
    ) + subdivide_until_under(
        chunk[mid:], meta, stem, max_bytes, chunk_count_placeholder
    )


def greedy_pack(
    items: list,
    meta: dict,
    stem: str,
    target_bytes: int,
    hard_max: int,
) -> list[list]:
    """Greedy batches, then subdivide any batch still over hard_max."""
    overhead = doc_size(meta, stem, 1, 999, [])
    batches: list[list] = []
    cur: list = []
    cur_sz = overhead

    for item in items:
        ib = json_bytes(item) + 1
        if cur and cur_sz + ib > target_bytes:
            batches.append(cur)
            cur = []
            cur_sz = overhead
        cur.append(item)
        cur_sz += ib
    if cur:
        batches.append(cur)

    out: list[list] = []
    for b in batches:
        out.extend(subdivide_until_under(b, meta, stem, hard_max, 999))
    return out


def split_file(path: Path, min_bytes: int, target_bytes: int, hard_max: int, dry_run: bool) -> int:
    if path.name == "manifest.json":
        return 0
    if is_part_file(path.name):
        return 0

    size = path.stat().st_size
    if size <= min_bytes:
        return 0

    text = path.read_text(encoding="utf-8")
    doc = json.loads(text)
    items = doc.get("data")
    if not isinstance(items, list):
        print(f"skip {path.name}: no data[] array")
        return 0

    stem = path.stem
    meta = {k: doc[k] for k in ("generatedAt", "source", "total", "successCount") if k in doc}

    chunks = greedy_pack(items, meta, stem, target_bytes, hard_max)
    n = len(chunks)

    for i, ch in enumerate(chunks, start=1):
        sz = doc_size(meta, stem, i, n, ch)
        if sz > hard_max and len(ch) == 1:
            print(f"warn: {path.stem}.part{i:03d}.json still {sz} bytes (single huge record)")

    if dry_run:
        print(f"[dry-run] {path.name} ({size} B) -> {n} parts")
        return n

    for i, ch in enumerate(chunks, start=1):
        out_name = f"{stem}.part{i:03d}.json"
        out_path = path.parent / out_name
        out_doc = {
            **meta,
            "chunkIndex": i,
            "chunkCount": n,
            "splitStem": stem,
            "data": ch,
        }
        out_path.write_text(dumps_compact(out_doc) + "\n", encoding="utf-8")

    path.unlink()
    print(f"split {path.name} ({size} B) -> {n} parts, removed original")
    return n


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--data-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "data",
    )
    ap.add_argument("--min-size", type=int, default=1 << 20, help="Split if file larger than this (bytes), default 1 MiB")
    ap.add_argument(
        "--target",
        type=int,
        default=int(1.75 * (1 << 20)),
        help="Greedy target batch size (~bytes), default ~1.75 MiB",
    )
    ap.add_argument(
        "--hard-max",
        type=int,
        default=2 << 20,
        help="Try to keep each part under this (bytes), default 2 MiB",
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    data_dir: Path = args.data_dir
    if not data_dir.is_dir():
        raise SystemExit(f"data dir not found: {data_dir}")

    json_files = sorted(data_dir.glob("*.json"), key=lambda p: p.name.lower())
    total_parts = 0
    for p in json_files:
        if p.name == "manifest.json":
            continue
        total_parts += split_file(p, args.min_size, args.target, args.hard_max, args.dry_run)

    if args.dry_run:
        print(f"dry-run done, would create ~{total_parts} part files total")


if __name__ == "__main__":
    main()
