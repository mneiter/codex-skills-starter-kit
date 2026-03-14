# Starter Kit Architecture

## Overview

This starter kit uses a three-layer skill model so that reusable Codex behavior can grow without collapsing into a single oversized workflow.

## Layer Roles

### Orchestration

Orchestration skills decide how work should begin and how it should flow. They normalize incoming tasks, select the right skills, and define clean handoffs.

### Guardrails

Guardrail skills keep work safe, bounded, and reviewable. They preserve progress, enforce shared boundaries, and ensure work is inspected before closure.

### Atomic

Atomic skills perform focused reusable tasks. They should solve one narrow problem well and remain easy to compose inside larger workflows.

## Why The Layers Matter

The layer model prevents common failure modes:

- intake logic leaking into task execution
- verification being skipped or buried inside implementation
- broad skills combining too many responsibilities
- project-specific needs polluting shared reusable assets

By separating concerns, the starter kit stays easier to maintain and easier to extend.

## Extension Model

The base kit is the shared foundation. New project-local skills or future technology packs should extend the system without modifying the meaning of canonical base skills.

Use these rules:

- add new reusable generic skills to the correct base layer only when they truly belong in the base kit
- add project-specific skills outside the canonical base folders
- add technology-specific packs under a separate namespace such as `packs/<pack-name>/`

## Design Principles

- prefer composable skills over monolithic workflows
- keep the base layer generic
- document availability through manifests and indexes
- make boundaries explicit so extension remains safe
