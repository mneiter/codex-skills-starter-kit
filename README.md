# Codex Skills Starter Kit

`codex-skills-starter-kit` is a reusable foundation repository for Codex skills. It keeps every discoverable skill under `.codex/skills`, separates canonical base skills from reusable plugins and project-specific skills, and makes the root skill registries the single global discovery surface for agents.

## Purpose

This repository exists to standardize a durable, reusable skill system:

- a canonical three-layer base architecture
- a global manifest and index for skill discovery
- reusable plugins that stay outside the base layer
- a reserved project area for repository-specific skills
- validation tooling, templates, and docs that keep the structure consistent

## Release Status

- `v1.0.0` is the first stable baseline of `codex-skills-starter-kit`.
- `main` continues as the active development line for `v1.1.0`.
- `release/1.0.0` is the frozen baseline for the first stable version.

## Canonical Skill Architecture

The repository now uses one canonical structure:

```text
.codex/
  skills/
    base/
      orchestration/
      guardrails/
      atomic/
    plugins/
      backend/
      frontend/
      platform/
      skill-development/
    project/
    skills-manifest.md
    skills-index.md
```

### Base Skills

Base skills are the shared foundation. They stay technology-agnostic and remain the only skills that belong in the canonical reusable starter kit.

The base layer keeps the responsibility model:

1. `orchestration`
2. `guardrails`
3. `atomic`

### Plugins

Plugins are reusable extensions that stay outside the base layer.

- actual plugins live under `.codex/skills/plugins/...`
- plugin groups such as `frontend`, `backend`, and `platform` are organizational containers only
- only plugins with real skills are registered in the root manifest and index

This repository currently includes:

- the actual plugin `.codex/skills/plugins/skill-development/`
- the plugin groups `.codex/skills/plugins/frontend/`, `.codex/skills/plugins/backend/`, and `.codex/skills/plugins/platform/`
- empty plugin scaffolds for future specialized plugins under those groups

### Project Skills

Project-specific skills belong under `.codex/skills/project/`. They are not part of the reusable base layer, but they still use the same responsibility tokens:

- `orchestration`
- `guardrails`
- `atomic`

## How To Use This Repository

1. Copy the starter kit into a new repository.
2. Keep the base skills intact under `.codex/skills/base/`.
3. Tailor the root `AGENTS.md`, onboarding docs, and root registries to the adopting project.
4. Add reusable extensions under `.codex/skills/plugins/` when they should stay outside the canonical base layer.
5. Add repository-specific skills under `.codex/skills/project/`.
6. Update `.codex/skills/skills-manifest.md` and `.codex/skills/skills-index.md` whenever the available skills change.

## What This Repository Intentionally Excludes

This starter kit does not ship:

- framework-specific or vendor-specific skills in the canonical base layer
- project-specific business context in the reusable repository root
- CI pipelines, licenses, or issue templates
- compatibility shims for old skill layouts

Those concerns belong either in project skills or in reusable plugins that do not alter the canonical base layer.

## Key Files

- `.codex/skills/skills-manifest.md` is the global skill registry.
- `.codex/skills/skills-index.md` is the global skill catalog.
- `templates/skill-template/SKILL.md` is the canonical authoring template.
- `docs/plugins/architecture.md` explains the plugin model.
- `docs/skills/skill-metadata.md` defines the normalized metadata contract.
- `docs/skills/validation.md` explains the repository validation workflow.
- `scripts/validate-skills` runs the validator.
- `STARTER_KIT_MANIFEST.md` defines what is canonical in this repository.

## Suggested Next Iteration

Reasonable v1.1 improvements include:

- external skill import workflow
- optional agent metadata generation for skills
- richer validation reporting or test fixtures
- populated plugin skills that build on the base kit without changing it
