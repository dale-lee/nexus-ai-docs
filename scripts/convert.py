"""Seed English source pages from the upstream Docusaurus guides.

Usage: uv run python scripts/convert.py /path/to/upstream-repo [out_dir]

Writes one Markdown file per mapped page into out_dir (default .seed/), with
Docusaurus frontmatter/imports stripped and :::admonitions converted to
MkDocs `!!!` blocks. Re-run on an upstream bump and diff the output against the
previous run to see what changed, then apply the changes to the Vietnamese
pages under docs/ (each carries an `<!-- upstream: ... -->` marker).
"""

import re
import subprocess
import sys
from pathlib import Path

# upstream page (relative to repo root) -> seed file name
MAPPING = {
    "docs/guides/dataset/configure_knowledge_base.md": "kho-tri-thuc/cau-hinh.md",
    "docs/guides/dataset/select_pdf_parser.md": "kho-tri-thuc/chon-bo-phan-tich-pdf.md",
    "docs/guides/dataset/run_retrieval_test.md": "kho-tri-thuc/kiem-tra-truy-hoi.md",
    "docs/guides/dataset/set_metadata.md": "kho-tri-thuc/metadata.set.md",
    "docs/guides/dataset/manage_metadata.md": "kho-tri-thuc/metadata.manage.md",
    "docs/guides/chat/start_chat.md": "hoi-dap/bat-dau.md",
    "docs/guides/ai_search.md": "tim-kiem.md",
    "docs/guides/agent/agent_introduction.md": "agent/gioi-thieu.md",
    "docs/guides/agent/embed_agent_into_webpage.md": "agent/nhung-vao-website.md",
    "docs/guides/manage_files.md": "tep.md",
    "docs/guides/team/join_or_leave_team.md": "nhom/tham-gia.md",
    "docs/guides/team/share_knowledge_bases.md": "nhom/chia-se.datasets.md",
    "docs/guides/team/share_agents.md": "nhom/chia-se.agents.md",
    "docs/faq.mdx": "cau-hoi-thuong-gap.md",
}

ADMONITION = {"note": "note", "tip": "tip", "info": "info", "caution": "warning", "danger": "danger"}


def convert(text: str) -> str:
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)  # frontmatter
    text = re.sub(r"^import .*\n", "", text, flags=re.M)
    out, block = [], None
    for line in text.splitlines():
        m = re.match(r"^:::(\w+)\s*(.*)$", line)
        if m and block is None:
            kind, title = ADMONITION.get(m.group(1), "note"), m.group(2).strip()
            out.append(f'!!! {kind} "{title}"' if title else f"!!! {kind}")
            block = kind
            continue
        if line.strip() == ":::" and block is not None:
            block = None
            continue
        out.append(("    " + line) if block and line else line)
    return "\n".join(out).strip() + "\n"


def main() -> None:
    repo = Path(sys.argv[1]).resolve()
    out_dir = Path(sys.argv[2] if len(sys.argv) > 2 else ".seed")
    commit = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "--short", "HEAD"], text=True).strip()
    for src, dst in MAPPING.items():
        target = out_dir / dst
        target.parent.mkdir(parents=True, exist_ok=True)
        body = convert((repo / src).read_text(encoding="utf-8"))
        target.write_text(f"<!-- upstream: {src} @ {commit} -->\n\n{body}", encoding="utf-8")
        print(f"{src} -> {target}")


if __name__ == "__main__":
    main()
