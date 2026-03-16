# Skill Development Direct Pack

## Purpose

This direct pack lives at `packs/skill-development/`. It is an optional extension for repositories that want extra guidance around creating, reviewing, and refining skills. It is not part of the canonical base layer.

## When To Use This Pack

Use this pack when a repository needs help with:

- creating a new skill from scratch
- reviewing whether an existing skill is well-scoped
- improving trigger descriptions
- deciding whether a skill needs more bundled resources
- deciding whether a skill should be split or moved into a pack

## When Not To Use This Pack

Do not use this pack for:

- normal repository task execution
- domain-specific implementation work unrelated to skill design
- replacing the canonical base skills
- carrying vendor-specific workflows into the base repository

## Boundaries

- This pack is an extension, not canonical base content.
- It must not relabel, replace, or modify the canonical base skills under `.codex/skills/`.
- It maintains its own manifest, index, references, and templates.
- It remains a direct pack rather than being placed inside a solution group because it is a cross-cutting workflow capability.

## Included Skills

- `author-skill`
- `evaluate-skill`
- `optimize-skill-description`

## Included Support Material

- reference guidance for evaluation and description improvement
- a reusable `skill-review-template.md` artifact for lightweight review cycles
