#!/usr/bin/env python3
"""
Build data/manifest.json (bundles) and regenerate data/index.html download list.
"""
from __future__ import annotations

import json
import re
import subprocess
import unicodedata
from pathlib import Path
from urllib.parse import quote, unquote

PART_RE = re.compile(r"^(.+)\.part(\d+)\.json$", re.IGNORECASE)
REPO = Path(__file__).resolve().parent.parent


def parse_index_titles(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    raw = path.read_text(encoding="utf-8")
    titles: dict[str, str] = {}
    pat = re.compile(r'<h2 class="dataset-name">([^<]+)</h2>[\s\S]*?href="\./([^"]+)"')
    for title, href in pat.findall(raw):
        fn = unicodedata.normalize("NFC", unquote(href))
        titles[fn] = title.strip()
    return titles


def load_titles_from_git_index() -> dict[str, str]:
    """filename.json -> display title (from last committed index if available)."""
    try:
        raw = subprocess.check_output(
            ["git", "show", "HEAD:data/index.html"],
            cwd=REPO,
            stderr=subprocess.DEVNULL,
        ).decode("utf-8")
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {}
    titles: dict[str, str] = {}
    pat = re.compile(r'<h2 class="dataset-name">([^<]+)</h2>[\s\S]*?href="\./([^"]+)"')
    for title, href in pat.findall(raw):
        fn = unicodedata.normalize("NFC", unquote(href))
        titles[fn] = title.strip()
    return titles


def human_label(stem: str) -> str:
    return stem.replace("-", " ").replace("_", " ").strip().title() + " Datası"


def collect_bundles(data_dir: Path, titles: dict[str, str]) -> list[dict]:
    singles: list[Path] = []
    groups: dict[str, list[tuple[int, Path]]] = {}

    for p in sorted(data_dir.glob("*.json"), key=lambda x: unicodedata.normalize("NFC", x.name).lower()):
        if p.name == "manifest.json":
            continue
        m = PART_RE.match(p.name)
        if m:
            stem = m.group(1)
            groups.setdefault(stem, []).append((int(m.group(2)), p))
        else:
            singles.append(p)

    bundles: list[dict] = []

    for p in singles:
        fn = unicodedata.normalize("NFC", p.name)
        label = titles.get(fn) or human_label(p.stem)
        bundles.append({"id": p.stem, "label": label, "files": [p.name]})

    for stem, items in sorted(groups.items()):
        items.sort(key=lambda x: x[0])
        files = [x[1].name for x in items]
        key = unicodedata.normalize("NFC", f"{stem}.json")
        label = titles.get(key) or human_label(stem)
        bundles.append({"id": stem, "label": label, "files": files})

    bundles.sort(key=lambda b: unicodedata.normalize("NFC", b["label"]).lower())
    return bundles


def write_manifest(data_dir: Path, bundles: list[dict]) -> None:
    out = {"bundles": bundles}
    (data_dir / "manifest.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_index_html(data_dir: Path, bundles: list[dict]) -> None:
    index_path = data_dir / "index.html"
    template_head = """<!doctype html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Data Kütüphanesi</title>
  <style>
    :root {
      --bg: #f5f5f7;
      --surface: #ffffff;
      --text: #1f1f22;
      --muted: #777780;
      --line: #ececef;
      --brand: #1c1c1e;
      --brand-hover: #2a2a2d;
      --radius: 12px;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      color: var(--text);
      background: var(--bg);
      min-height: 100vh;
      padding: 44px 18px;
    }

    .container {
      max-width: 900px;
      margin: 0 auto;
    }

    .header {
      margin-bottom: 14px;
    }

    .header-browse {
      margin-top: 10px;
      font-size: 13px;
    }

    .header-browse a {
      color: var(--brand);
      font-weight: 600;
      text-decoration: underline;
      text-underline-offset: 3px;
    }

    h1 {
      margin: 0 0 8px;
      font-size: clamp(16px, 3vw, 24px);
      letter-spacing: -0.02em;
    }

    .panel {
      margin-top: 20px;
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 12px;
    }

    .row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--surface);
      gap: 10px;
      padding: 13px 14px;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      box-shadow: 0 4px 14px rgba(15, 15, 20, 0.04);
    }

    .row:hover {
      background-color: #f4f5f6;
    }

    .dataset-name {
      margin: 0 0 3px;
      font-size: 14px;
      font-weight: 600;
    }

    .dataset-meta {
      margin: 0;
      font-size: 12px;
      color: var(--muted);
    }

    .download-btn {
      border: 0;
      border-radius: 8px;
      background: var(--brand);
      color: #fff;
      text-decoration: none;
      font-weight: 600;
      font-size: 12px;
      padding: 8px 12px;
      white-space: nowrap;
      transition: background 0.18s ease, transform 0.18s ease;
    }

    .download-btn:hover {
      background: var(--brand-hover);
      transform: translateY(-1px);
    }

    .download-btn:active {
      transform: translateY(0);
    }

    @media (max-width: 640px) {
      .panel {
        grid-template-columns: 1fr;
      }

      .row {
        flex-direction: column;
        align-items: flex-start;
      }

      .download-btn {
        width: 100%;
        text-align: center;
      }
    }
  </style>
</head>
<body>
  <main class="container">
    <header class="header">
      <h1>JSON Dataset Listesi</h1>
      <p class="header-browse"><a href="./browse.html">Gözat ve ara →</a></p>
    </header>

    <section class="panel" aria-label="Dataset listesi">
"""

    template_tail = """    </section>

  </main>
</body>
</html>
"""

    rows: list[str] = []
    for b in bundles:
        n = len(b["files"])
        for i, fn in enumerate(b["files"], start=1):
            href = "./" + quote(fn, safe="/")
            if n == 1:
                label = b["label"]
            else:
                short = b["label"].replace(" Datası", "").strip()
                label = f"{short} — parça {i}/{n}"
            rows.append("      <article class=\"row\">")
            rows.append("        <div>")
            rows.append(f"          <h2 class=\"dataset-name\">{label}</h2>")
            rows.append("          <p class=\"dataset-meta\">Format: JSON</p>")
            rows.append("        </div>")
            rows.append(f"        <a class=\"download-btn\" href=\"{href}\" download>Download</a>")
            rows.append("      </article>")

    index_path.write_text(template_head + "\n".join(rows) + "\n" + template_tail, encoding="utf-8")


def main() -> None:
    data_dir = REPO / "data"
    titles = {**load_titles_from_git_index(), **parse_index_titles(data_dir / "index.html")}
    bundles = collect_bundles(data_dir, titles)
    write_manifest(data_dir, bundles)
    write_index_html(data_dir, bundles)
    print(f"manifest + index: {len(bundles)} bundles")


if __name__ == "__main__":
    main()
