#!/usr/bin/env python3
"""Render Trading OS reports.

Finds every runs/**/report.md file and creates matching report.html files.
If Chrome is available, also creates report.pdf using headless Chrome.
Finally builds site/index.html with links to all reports.
"""

from __future__ import annotations

import html
import os
import pathlib
import shutil
import subprocess
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
RUNS = ROOT / "runs"
SITE = ROOT / "site"


def md_to_html_text(markdown_text: str) -> str:
    try:
        import markdown  # type: ignore
        body = markdown.markdown(markdown_text, extensions=["tables", "fenced_code", "toc"])
    except Exception:
        escaped = html.escape(markdown_text)
        body = "<pre>" + escaped + "</pre>"
    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Trading OS Report</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif; margin: 40px auto; max-width: 980px; line-height: 1.55; color: #111; }}
    h1, h2, h3 {{ line-height: 1.2; }}
    table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
    th, td {{ border: 1px solid #ddd; padding: 8px; vertical-align: top; }}
    th {{ background: #f6f6f6; }}
    code, pre {{ background: #f6f6f6; padding: 2px 4px; border-radius: 4px; }}
    pre {{ padding: 12px; overflow-x: auto; }}
    blockquote {{ border-left: 4px solid #ddd; padding-left: 12px; color: #444; }}
    .meta {{ color: #666; font-size: 0.92em; }}
  </style>
</head>
<body>
{body}
</body>
</html>
"""


def find_chrome() -> str | None:
    for name in ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser"]:
        path = shutil.which(name)
        if path:
            return path
    return None


def render_pdf(chrome: str, html_path: pathlib.Path, pdf_path: pathlib.Path) -> None:
    subprocess.run(
        [
            chrome,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ],
        check=True,
    )


def render_reports() -> list[pathlib.Path]:
    reports = sorted(RUNS.glob("**/report.md")) if RUNS.exists() else []
    chrome = find_chrome()
    for md_path in reports:
        text = md_path.read_text(encoding="utf-8")
        html_path = md_path.with_suffix(".html")
        pdf_path = md_path.with_suffix(".pdf")
        html_path.write_text(md_to_html_text(text), encoding="utf-8")
        if chrome:
            try:
                render_pdf(chrome, html_path, pdf_path)
            except Exception as exc:
                print(f"PDF render failed for {md_path}: {exc}")
        else:
            print("Chrome not found; skipped PDF rendering")
    return reports


def build_index(reports: list[pathlib.Path]) -> None:
    SITE.mkdir(exist_ok=True)
    rows = []
    for md_path in sorted(reports, reverse=True):
        rel_dir = md_path.parent.relative_to(ROOT)
        html_rel = rel_dir / "report.html"
        pdf_rel = rel_dir / "report.pdf"
        md_rel = rel_dir / "report.md"
        title = "/".join(rel_dir.parts)
        rows.append(
            f"<tr><td>{html.escape(title)}</td>"
            f"<td><a href='../{html_rel.as_posix()}'>HTML</a></td>"
            f"<td><a href='../{pdf_rel.as_posix()}'>PDF</a></td>"
            f"<td><a href='../{md_rel.as_posix()}'>MD</a></td></tr>"
        )
    body = "\n".join(rows) or "<tr><td colspan='4'>No reports yet.</td></tr>"
    index = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Trading OS Reports</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif; margin: 40px auto; max-width: 980px; line-height: 1.55; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border: 1px solid #ddd; padding: 8px; }}
    th {{ background: #f6f6f6; }}
  </style>
</head>
<body>
  <h1>Trading OS Reports</h1>
  <p>Generated {datetime.utcnow().isoformat(timespec='seconds')}Z.</p>
  <table>
    <thead><tr><th>Report</th><th>HTML</th><th>PDF</th><th>Markdown</th></tr></thead>
    <tbody>{body}</tbody>
  </table>
</body>
</html>
"""
    (SITE / "index.html").write_text(index, encoding="utf-8")


def main() -> None:
    reports = render_reports()
    build_index(reports)


if __name__ == "__main__":
    main()
