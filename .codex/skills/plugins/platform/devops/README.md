# Devops Plugin

## Purpose

This plugin lives at `.codex/skills/plugins/platform/devops/`. It is a reusable extension for GitHub-centered and Docker-centered operational workflows that do not belong in the canonical base layer.

## When To Use This Plugin

Use this plugin when a repository needs help with:

- GitHub workflow state inspection
- Dockerfile, image, container, or compose-context triage
- pull request and issue lifecycle triage
- blocked pull request summaries and next-step guidance
- container startup or image-hygiene diagnosis
- review feedback clustering
- bounded GitHub-side metadata actions with explicit targets
- bounded Docker-side inspection with explicit targets

## When Not To Use This Plugin

Do not use this plugin for:

- multi-skill workflow orchestration
- validation execution or test interpretation
- repair loops or refactoring work
- reviewer-facing pull request narratives
- GitHub Actions authoring or workflow editing
- Kubernetes or infrastructure orchestration
- deployment, infrastructure execution, or other broad DevOps operations

## Boundaries

- This plugin is an extension, not canonical base content.
- `.codex/skills/plugins/platform/` remains a plugin group and keeps only `README.md`.
- `.codex/skills/plugins/platform/devops/` is the actual plugin root and owns its local catalogs.
- Keep GitHub-specific, Docker-specific, and DevOps-specific guidance out of the canonical base skills.

## Included Skills

- `github-operations`
- `docker-operations`
