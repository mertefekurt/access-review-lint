from __future__ import annotations

from access_review_lint.models import Rule

PROJECT_NAME = 'access-review-lint'
SUMMARY = 'Lint access review exports for stale admins and missing justification.'
SAMPLE_RISK = 'user admin last_seen 2024 justification missing'
SAMPLE_CLEAN = 'user viewer last_seen 2026 justification support access'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='stale-admin',
        severity='high',
        pattern='admin.{0,40}last_seen\\s+20(1[0-9]|2[0-4])',
        message='stale admin access detected',
        recommendation='remove or reapprove privileged access',
    ),
    Rule(
        code='missing-justification',
        severity='medium',
        pattern='justification\\s+(missing|none|unknown)',
        message='access justification is missing',
        recommendation='record business reason',
    ),
    Rule(
        code='broad-role',
        severity='low',
        pattern='\\b(admin|owner|superuser)\\b',
        message='broad role detected',
        recommendation='check least privilege',
    ),
)
