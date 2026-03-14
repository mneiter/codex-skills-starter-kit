# Starter Kit Manifest

## Purpose

This document defines the canonical contents and boundaries of `codex-skills-starter-kit`. It is the source of truth for what belongs in the reusable base repository and how future extensions should be added.

## Canonical Contents

The following repository elements are canonical:

- the three base skill layers under `.codex/skills/`
- the nine base skills shipped in those layers
- `.codex/skills/skills-manifest.md` as the canonical registry
- `.codex/skills/skills-index.md` as the quick discovery catalog
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
- templates and documentation that help teams adopt and extend the starter kit
- examples that demonstrate usage without encoding project-specific logic

### What Must Stay Out Of The Base Kit

- framework-specific or language-specific packs
- frontend-only, backend-only, infrastructure-only, or vendor-tied skills
- project-specific business logic, domain rules, or organization policies
- local repository commands, scripts, or workflows that assume a specific toolchain

### Future Pack Policy

Future technology packs must be added without polluting the canonical base layer.

- Place technology-specific packs under a separate namespace such as `packs/<pack-name>/`, or publish them in a separate repository.
- Give each pack its own manifest, index, and supporting documentation.
- Do not modify, rename, or relabel canonical base skills to fit a pack.
- Treat the base kit as the shared foundation and packs as additive extensions.

## Maintenance Expectations

When this repository changes:

- keep the manifest and index accurate
- preserve the layer model
- keep all content in English
- avoid widening scope unless the addition is reusable and belongs in the base kit
