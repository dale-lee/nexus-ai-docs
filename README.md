# Nexus AI — Hướng dẫn sử dụng

Published at https://dale-lee.github.io/nexus-ai-docs/

## Develop

```bash
uv sync
uv run mkdocs serve          # http://127.0.0.1:8000
uv run mkdocs build --strict # what CI runs
```

Pushing to `main` deploys to GitHub Pages via `.github/workflows/deploy.yml`.

## Layout

- `docs/` — Vietnamese pages, one per user flow. Each page starts with an
  `<!-- upstream: ... -->` marker naming the source page and commit it was
  adapted from.
- `docs/img/<page>/` — screenshots, referenced relatively from the pages.
- `scripts/convert.py` — seeds English source pages from the upstream repo
  into `.seed/` (gitignored). On an upstream docs bump, run it, diff `.seed/`
  against the previous run, and apply the changes to the pages in `docs/`.
