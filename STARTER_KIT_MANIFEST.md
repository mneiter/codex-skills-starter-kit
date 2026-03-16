# Starter Kit Manifest

## Purpose

This document defines the canonical contents and boundaries of `codex-skills-starter-kit`. It is the source of truth for what belongs in the reusable base repository and how future extensions should be added.

## Canonical Contents

The following repository elements are canonical:

- the three base skill layers under `.codex/skills/base/`
- the nine base skills shipped in those layers
- `.codex/skills/skills-manifest.md` as the global skill registry
- `.codex/skills/skills-index.md` as the global discovery catalog
- the plugin scaffolding and plugin documentation under `.codex/skills/plugins/` and `docs/plugins/`
- the reserved project area under `.codex/skills/project/`
- the validation entrypoint at `scripts/validate-skills`
- the validator tooling and schema under `tools/skill-validator/`
- the starter templates under `templates/`
- the architecture, conventions, and workflow documentation under `docs/`
- the minimal adoption example under `examples/minimal-project/`
- the root `README.md` and `AGENTS.md`

## Canonical Base Skills

### Orchestration

- `task-intake-supervisor`
- `skill-router`

### Guardrails

- `execution-memory-loop`
- `review-and-repair-loop`
- `shared-boundary-guardrails`

### Atomic

- `ci-verification`
- `generate-pull-request`
- `refactor-feature`
- `unit-tests`

## Stability Rules

- Base skill names are stable identifiers and should only change with a deliberate repository-wide update.
- Base skills must remain technology-agnostic.
- Manifests, indexes, templates, and documentation must stay aligned with the canonical base skills.
- Example files may illustrate adoption patterns, but they must not redefine the canonical base layer.

## Boundaries

### What Belongs In The Base Kit

- reusable skills that apply across many repositories
- stack-agnostic orchestration, guardrails, and atomic task guidance
- tooling and schemas that validate the shared skill system
- templates and documentation that help teams adopt and extend the starter kit
- examples that demonstrate usage without encoding project-specific logic
- plugin scaffolding that reserves reusable extension points without changing base skills
- the reserved `project/` location that shows where project-specific skills belong

### What Must Stay Out Of The Base Kit

- framework-specific or language-specific skill content inside the canonical base layer
- project-specific content inside the reusable base layer
- project-specific business logic, domain rules, or organization policies
- local repository commands, scripts, or workflows that assume a specific toolchain

### Future Plugin Policy

Future plugins must be added without polluting the canonical base layer.

- Plugins are extensions, not canonical base content.
- Use `.codex/skills/plugins/<plugin-name>/` for reusable cross-cutting plugins such as `.codex/skills/plugins/skill-development/`.
- Use `.codex/skills/plugins/<group>/` as a lightweight plugin group only.
- Use `.codex/skills/plugins/<group>/<plugin-name>/` for grouped plugin locations such as `.codex/skills/plugins/frontend/angular/` or `.codex/skills/plugins/backend/python/`.
- Keep plugin groups lightweight and limited to `README.md`.
- Keep `plugin-manifest.md` and `plugin-index.md` only inside actual plugin roots that contain skills.
- Plugins must not modify, rename, or relabel canonical base skills to fit a plugin.
- Empty plugin scaffolds are allowed as canonical infrastructure, but they are not globally registered until they contain skills.
- Treat the base kit as the shared foundation, plugins as reusable extensions, and `project/` as repository-local space.

## Maintenance Expectations

When this repository changes:

- keep the manifest and index accurate
- keep the validator and metadata schema aligned with the documented skill model
- preserve the layer model
- keep all content in English
- avoid widening scope unless the addition is reusable and belongs in the base kit
