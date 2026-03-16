# Pack Architecture

## Purpose

Packs are the repository's extension mechanism for technology-specific or domain-specific skill content. They let the starter kit grow without changing the canonical base layer under `.codex/skills/`.

## Two-Axis Model

The starter kit now uses two complementary axes:

1. Responsibility layer
   - `orchestration`
   - `guardrails`
   - `atomic`
2. Pack grouping
   - technology or domain-specific extension namespaces under `packs/`

Layer and pack are not the same thing:

- layer describes what responsibility a skill performs
- pack describes where a specialized skill belongs organizationally
- one pack may contain orchestration, guardrails, and atomic skills

## Pack Boundaries

- packs are extensions, not canonical base content
- packs must not relabel, replace, or absorb canonical base skills
- packs keep their own manifest, index, and supporting documentation
- empty pack scaffolds are allowed as extension points

## Standard Pack Root

Each pack root should contain:

- `README.md`
- `skills-manifest.md`
- `skills-index.md`

## Optional Pack Layout

Packs may also contain:

```text
pack-name/
  README.md
  skills-manifest.md
  skills-index.md
  skills/
  examples/
  docs/
  rules/
```

Use these optional directories only when the pack has real content to place there.

## How Packs Extend The Base Kit

Use packs when:

- a skill is useful across a class of repositories but not generic enough for the base layer
- examples or references need technology-specific context
- extension rules are needed for one ecosystem without leaking into the shared base

Do not use packs to:

- move generic base skills out of `.codex/skills/`
- bypass the canonical layer model
- hide project-specific business logic that belongs only in one repository

## Current Pack Scaffold

This repository currently includes:

- `packs/skill-development/` as an active extension pack
- `packs/angular/`, `packs/react/`, `packs/python/`, and `packs/devops/` as empty scaffolds for future technology packs
