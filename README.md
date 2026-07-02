# access-review-lint

> Lint access review exports for stale admins and missing justification.

## Risk note Overview

Lint access review exports for stale admins and missing justification. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts access review notes. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
access-review-lint examples/sample.txt
access-review-lint examples/sample.txt --json --fail-on medium
python -m access_review_lint --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `stale-admin` | high | stale admin access detected |
| `missing-justification` | medium | access justification is missing |
| `broad-role` | low | broad role detected |

## Validation Notes

```bash
ruff check .
pytest
python -m access_review_lint --help
```

Example risky input:

```text
user admin last_seen 2024 justification missing
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
