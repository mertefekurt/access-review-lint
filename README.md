# Access Review Lint

Lint access review exports for stale admins and missing justification. The repository is intentionally plain: a small command, a visible rule surface, and enough examples to make the behavior inspectable.

<img src="assets/readme-cover.svg" alt="Access Review Lint cover" width="100%" />

## Review checklist

- [ ] stale admin access detected (`stale-admin`, high)
- [ ] access justification is missing (`missing-justification`, medium)
- [ ] broad role detected (`broad-role`, low)

## Command path

```bash
git clone https://github.com/mertefekurt/access-review-lint.git
cd access-review-lint
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
access-review-lint examples/sample.txt
access-review-lint examples/sample.txt --json
```

## Fixture worth keeping

```text
user admin last_seen 2024 justification missing
```

## Files I look at first

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
