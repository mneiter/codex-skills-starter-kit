# Codex Skills Starter Kit

`codex-skills-starter-kit` is a reusable foundation repository for storing technology-agnostic Codex skills. It provides a clean base layer that can be copied into future projects and then extended with project-local skills or separate technology packs.

## Purpose

This repository exists to standardize the minimum durable structure for Codex skills:

- a canonical three-layer skill architecture
- a small base set of reusable skills
- manifest and index files for discovery
- templates for future skill authoring and project adoption
- documentation that explains how to extend the kit without polluting the base layer

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

docs/
  architecture/
  conventions/
  workflows/

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
4. Add project-local skills beside the base layer, or add technology packs under a separate namespace such as `packs/<pack-name>/`.
5. Update the manifest and index whenever the available skills change.

## What This Repository Intentionally Excludes

This starter kit does not ship:

- framework-specific skills
- frontend-specific or backend-specific packs
- vendor-specific workflows
- project-specific business context
- CI pipelines, licenses, or issue templates

Those concerns belong either in the adopting repository or in separate add-on packs that do not modify the canonical base layer.

## Key Files

- `.codex/skills/skills-manifest.md` is the canonical active-skill registry.
- `.codex/skills/skills-index.md` is the quick catalog for discovery.
- `templates/skill-template/SKILL.md` is the canonical authoring template.
- `STARTER_KIT_MANIFEST.md` defines what is canonical in this repository.

## Suggested Next Iteration

Reasonable v1.1 improvements include:

- automated validation for manifest and section consistency
- optional agent metadata generation for skills
- separate technology packs that build on the base kit without changing it
