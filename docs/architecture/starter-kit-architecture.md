# Starter Kit Architecture

## Overview

This starter kit uses two complementary organizational axes:

- the canonical responsibility layer model for base skills
- the pack model for specialized extensions

## Base Skills

The canonical base skills live under `.codex/skills/` and remain independent from packs.

### Orchestration

Orchestration skills decide how work should begin and how it should flow. They normalize incoming tasks, select the right skills, and define clean handoffs.

### Guardrails

Guardrail skills keep work safe, bounded, and reviewable. They preserve progress, enforce shared boundaries, and ensure work is inspected before closure.

### Atomic

Atomic skills perform focused reusable tasks. They should solve one narrow problem well and remain easy to compose inside larger workflows.

## Pack Model

Packs are the second axis of organization.

- a `direct pack` lives at `packs/<pack-name>/`
- a `solution group` lives at `packs/<group>/`
- a `leaf pack` lives at `packs/<group>/<pack-name>/`

Pack placement does not replace layer classification. A direct pack or leaf pack may contain orchestration, guardrails, and atomic skills.

## Why The Two Axes Matter

The two axes help prevent:

- base skills becoming specialized or stack-bound
- specialized packs pretending to be part of the canonical base layer
- large workflows mixing responsibility classification with organizational grouping
- pack sprawl without clear functional boundaries

## Extension Model

Use these rules:

- add new reusable generic skills to the correct base layer only when they truly belong in the shared foundation
- add project-specific skills outside the canonical base folders
- add cross-cutting extensions as direct packs such as `packs/skill-development/`
- add specialized packs under solution groups such as `packs/frontend/angular/`
- keep solution groups lightweight and keep manifests and indexes only at direct-pack and leaf-pack roots

## Canonical Examples

- `packs/skill-development/`
- `packs/frontend/angular/`
- `packs/frontend/react/`
- `packs/backend/python/`
- `packs/backend/dotnet/`
- `packs/platform/devops/`
