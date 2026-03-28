# Data Plugin Manifest

This manifest lists the skills included in the plugin `.codex/skills/plugins/platform/data/`.

## Status Values

- `active`: approved and recommended for normal use
- `experimental`: available for trial use but not yet stable
- `deprecated`: still present but scheduled for replacement or removal
- `retired`: kept only for historical reference and not recommended for use

## Skills

| Skill | Layer | Status | Path | Purpose |
| --- | --- | --- | --- | --- |
| postgres-operations | atomic | active | `.codex/skills/plugins/platform/data/skills/postgres-operations/SKILL.md` | Manage PostgreSQL operational state across sessions, queries, locks, indexes, and schema-risk signals while keeping adjacent execution concerns separate. |
