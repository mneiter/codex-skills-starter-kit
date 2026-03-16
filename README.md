# Codex Skills Starter Kit

`codex-skills-starter-kit` is a reusable foundation repository for storing technology-agnostic Codex skills. It provides a clean base layer that can be copied into future projects and then extended with project-local skills, direct packs, or specialized packs organized under solution groups.

## Purpose

This repository exists to standardize the minimum durable structure for Codex skills:

- a canonical three-layer skill architecture
- a small base set of reusable skills
- manifest and index files for discovery
- templates for future skill authoring and project adoption
- documentation that explains how to extend the kit without polluting the base layer
- optional extension packs that can add specialized guidance without changing the base layer

## Release Status

- `v1.0.0` is the first stable baseline of `codex-skills-starter-kit`.
- `main` continues as the active development line for the next iteration, `v1.1.0`.
- `release/1.0.0` represents the frozen baseline for the first stable version.

## Canonical Layer Model

The base kit organizes skills into three layers:

1. `orchestration`
   Coordinate intake, routing, sequencing, and handoff between other skills.
2. `guardrails`
   Keep execution safe, reviewable, and bounded through shared verification and operating rules.
3. `atomic`
   Handle focused reusable tasks such as validation, test creation, refactoring, and pull request drafting.

This separation keeps responsibilities clear and makes the skill system easier to extend without turning a single skill into an unstructured workflow bundle.

## Repository Structure

```text
.codex/
  skills/
    orchestration/
    guardrails/
    atomic/
    skills-manifest.md
    skills-index.md

templates/
  skill-template/
  agents/
  manifests/
  docs/

packs/
  backend/
    README.md
    dotnet/
    python/
  frontend/
    README.md
    angular/
    react/
  platform/
    README.md
    devops/
  skill-development/

docs/
  architecture/
  conventions/
  packs/
  releases/
  skills/
  workflows/

scripts/
  validate-skills

tools/
  skill-validator/

examples/
  minimal-project/

AGENTS.md
README.md
STARTER_KIT_MANIFEST.md
```

## Base Skills

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

## How To Use This Repository

1. Copy the starter kit into a new repository.
2. Keep the base skills intact as the canonical reusable layer.
3. Tailor the root `AGENTS.md`, onboarding docs, and manifests to the adopting project.
4. Add project-local skills beside the base layer, or add optional extensions as either direct packs like `packs/skill-development/` or leaf packs such as `packs/frontend/angular/`.
5. Update the manifest and index whenever the available skills change.

## Optional Packs

Optional packs are additive extensions. They are useful when a repository needs reusable guidance that should not become part of the canonical base layer.

Use these canonical terms:

- `base skills`: `.codex/skills/`
- `direct pack`: `packs/<pack-name>/`
- `solution group`: `packs/<group>/`
- `leaf pack`: `packs/<group>/<pack-name>/`

- packs are not canonical base content
- packs must not relabel or replace canonical base skills
- packs must maintain their own manifest, index, and supporting docs

This repository now includes:

- the direct pack `packs/skill-development/`
- the solution groups `packs/frontend/`, `packs/backend/`, and `packs/platform/`
- the leaf packs `packs/frontend/angular/`, `packs/frontend/react/`, `packs/backend/python/`, `packs/backend/dotnet/`, and `packs/platform/devops/`

## What This Repository Intentionally Excludes

This starter kit does not ship:

- framework-specific skills in the canonical base layer
- populated specialized pack content that does not belong in this starter-kit repository
- vendor-specific workflows
- project-specific business context
- CI pipelines, licenses, or issue templates

Those concerns belong either in the adopting repository or in separate add-on packs that do not modify the canonical base layer.

## Key Files

- `.codex/skills/skills-manifest.md` is the canonical active-skill registry.
- `.codex/skills/skills-index.md` is the quick catalog for discovery.
- `templates/skill-template/SKILL.md` is the canonical authoring template.
- `STARTER_KIT_MANIFEST.md` defines what is canonical in this repository.
- `docs/skills/skill-metadata.md` defines the normalized metadata contract for skills.
- `docs/skills/validation.md` explains the repository validation workflow.
- `docs/packs/architecture.md` explains how direct packs, solution groups, and leaf packs extend the starter kit.
- `scripts/validate-skills` runs the skill validator.
- `packs/skill-development/README.md` explains the optional skill-development extension pack.

## Suggested Next Iteration

Reasonable v1.1 improvements include:

- external skill import workflow
- optional agent metadata generation for skills
- richer validation reporting or test fixtures
- populated leaf packs that build on the base kit without changing it
