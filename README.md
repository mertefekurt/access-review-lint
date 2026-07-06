<img src="assets/readme-cover.svg" alt="Access Review Lint cover" width="100%" />

# Access Review Lint

Lint access review exports for stale admins and missing justification.

![stack](https://img.shields.io/badge/stack-Python-dc2626?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-7c3aed?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-0891b2?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-b45309?style=flat-square)

## Workflow

1. Collect the review notes or exported records.
2. Run `access-review-lint` against the file.
3. Read the findings in Markdown, or switch to JSON for automation.
4. Fail CI only at the severity level you care about.

## Checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `stale-admin` | high | stale admin access detected |
| `missing-justification` | medium | access justification is missing |
| `broad-role` | low | broad role detected |

## Command line

```bash
python -m pip install -e ".[dev]"
access-review-lint examples/sample.txt
access-review-lint examples/sample.txt --json --fail-on medium
```

## Sample risky input

```text
user admin last_seen 2024 justification missing
```

## Project shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
