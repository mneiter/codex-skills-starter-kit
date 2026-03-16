# Starter Kit Architecture

## Overview

This starter kit organizes skills under one canonical root:

- `base skills` in `.codex/skills/base/`
- reusable `plugins` in `.codex/skills/plugins/`
- repository-specific `project skills` in `.codex/skills/project/`

Responsibility classification still uses the same three layer tokens:

- `orchestration`
- `guardrails`
- `atomic`

Scope placement does not replace layer classification. A plugin skill or a project skill still uses one of the same three layers.

## Base Skills

Base skills are the canonical reusable foundation.

### Orchestration

Orchestration skills decide how work should begin and how it should flow. They normalize incoming tasks, select the right skills, and define clean handoffs.

### Guardrails

Guardrail skills keep work safe, bounded, and reviewable. They preserve progress, enforce shared boundaries, and ensure work is inspected before closure.

### Atomic

Atomic skills perform focused reusable tasks. They should solve one narrow problem well and remain easy to compose inside larger workflows.

## Plugin Model

Plugins are reusable extensions that stay outside the base layer.

- a cross-cutting plugin may live directly under `.codex/skills/plugins/<plugin-name>/`
- a `plugin group` may live at `.codex/skills/plugins/<group>/`
- a grouped plugin may live at `.codex/skills/plugins/<group>/<plugin-name>/`

Plugin groups are organizational containers only. They are not plugins, they do not appear in the root registries, and they do not contain manifests or indexes.

Only actual plugin roots that contain skills have:

- `plugin-manifest.md`
- `plugin-index.md`
- `skills/`

## Project Skills

Project skills are repository-local additions. They live under `.codex/skills/project/`, stay out of the reusable base layer, and are still registered in the root manifest and index when they exist.

## Why The Model Matters

This structure helps prevent:

- base skills becoming specialized or project-bound
- reusable plugins pretending to be part of the canonical base layer
- project-specific knowledge leaking into shared reusable skills
- fragmented discovery surfaces outside `.codex/skills/`

## Extension Rules

- add new reusable generic skills to `.codex/skills/base/` only when they truly belong in the shared foundation
- add reusable specialized extensions under `.codex/skills/plugins/`
- add repository-specific skills under `.codex/skills/project/`
- keep plugin groups lightweight and keep plugin catalogs only at actual plugin roots
- keep `.codex/skills/skills-manifest.md` and `.codex/skills/skills-index.md` as the single global discovery surface

## Canonical Examples

- `.codex/skills/plugins/skill-development/`
- `.codex/skills/plugins/frontend/angular/`
- `.codex/skills/plugins/frontend/react/`
- `.codex/skills/plugins/backend/python/`
- `.codex/skills/plugins/backend/dotnet/`
- `.codex/skills/plugins/platform/devops/`
