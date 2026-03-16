# Starter Kit Architecture

## Overview

This starter kit uses two complementary organizational axes so reusable Codex behavior can grow without collapsing into a single oversized workflow:

- the canonical responsibility layer model
- optional pack grouping for technology or domain-specific extensions

## Responsibility Layers

### Orchestration

Orchestration skills decide how work should begin and how it should flow. They normalize incoming tasks, select the right skills, and define clean handoffs.

### Guardrails

Guardrail skills keep work safe, bounded, and reviewable. They preserve progress, enforce shared boundaries, and ensure work is inspected before closure.

### Atomic

Atomic skills perform focused reusable tasks. They should solve one narrow problem well and remain easy to compose inside larger workflows.

## Optional Pack Grouping

Packs group skills and supporting material by technology or domain without changing the meaning of the canonical base layer. Pack membership is separate from layer classification.

- a pack may contain orchestration, guardrails, and atomic skills
- pack membership tells you where a skill belongs organizationally
- layer tells you what responsibility the skill performs
- packs are extensions and must not replace or relabel canonical base skills

## Why The Two Axes Matter

The layer model and pack model together prevent common failure modes:

- intake logic leaking into task execution
- verification being skipped or buried inside implementation
- broad skills combining too many responsibilities
- project-specific needs polluting shared reusable assets
- extension content pretending to be part of the canonical base layer

By separating concerns, the starter kit stays easier to maintain and easier to extend.

## Extension Model

The base kit is the shared foundation. New project-local skills or optional packs should extend the system without modifying the meaning of canonical base skills.

Use these rules:

- add new reusable generic skills to the correct base layer only when they truly belong in the base kit
- add project-specific skills outside the canonical base folders
- add optional packs under a separate namespace such as `packs/<pack-name>/`
- keep pack manifests, indexes, and docs separate from the canonical base catalogs

Optional packs are non-canonical extensions. They may add their own skills, templates, references, and docs, but they must not relabel, replace, or absorb the canonical base skills under `.codex/skills/`.

## Design Principles

- prefer composable skills over monolithic workflows
- keep the base layer generic
- keep pack scaffolds explicit so future extension points are obvious
- document availability through manifests and indexes
- make boundaries explicit so extension remains safe
