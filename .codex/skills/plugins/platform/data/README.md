# Data Plugin

## Purpose

This plugin lives at `.codex/skills/plugins/platform/data/`. It is a reusable extension for data and database operational diagnosis that does not belong in the canonical base layer.

## When To Use This Plugin

Use this plugin when a repository needs help with:

- PostgreSQL operational state inspection
- slow-query, lock, or connection triage
- index-usage and plan interpretation
- schema-risk or migration-risk review at a diagnostic level
- safe database-side evidence gathering without destructive action

## When Not To Use This Plugin

Do not use this plugin for:

- multi-skill workflow orchestration
- validation execution or readiness evidence
- repair loops or refactoring work
- reviewer-facing pull request narratives
- destructive database changes or full DBA ownership
- application-layer bug fixing

## Boundaries

- This plugin is an extension, not canonical base content.
- `.codex/skills/plugins/platform/` remains a plugin group and keeps only `README.md`.
- `.codex/skills/plugins/platform/data/` is the actual plugin root and owns its local catalogs.
- Keep database-specific and data-operations guidance out of the canonical base skills.
- This plugin starts with PostgreSQL but its structure should scale cleanly to additional data-oriented skills later.

## Included Skills

- `postgres-operations`
