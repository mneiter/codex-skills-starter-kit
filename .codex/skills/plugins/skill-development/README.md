# Skill Development Plugin

## Purpose

This plugin lives at `.codex/skills/plugins/skill-development/`. It is a reusable extension for repositories that want extra guidance around creating, reviewing, and refining skills. It is not part of the canonical base layer.

## When To Use This Plugin

Use this plugin when a repository needs help with:

- creating a new skill from scratch
- reviewing whether an existing skill is well-scoped
- improving trigger descriptions
- deciding whether a skill needs more bundled resources
- deciding whether a skill should be split or moved out of one scope into another

## When Not To Use This Plugin

Do not use this plugin for:

- normal repository task execution
- domain-specific implementation work unrelated to skill design
- replacing the canonical base skills
- carrying vendor-specific workflows into the base repository

## Boundaries

- This plugin is an extension, not canonical base content.
- It must not relabel, replace, or modify the canonical base skills under `.codex/skills/base/`.
- It maintains its own plugin manifest, plugin index, references, and templates.
- It remains a top-level plugin because it is a cross-cutting workflow capability rather than a grouped specialized extension.

## Included Skills

- `author-skill`
- `evaluate-skill`
- `optimize-skill-description`

## Included Support Material

- reference guidance for evaluation and description improvement
- a reusable `skill-review-template.md` artifact for lightweight review cycles
