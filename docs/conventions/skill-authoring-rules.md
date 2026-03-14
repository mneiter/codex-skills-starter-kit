# Skill Authoring Rules

## Core Rules

- Keep all content in English.
- Write `SKILL.md` frontmatter with only `name` and `description`.
- Keep the description clear about what the skill does and when it should be used.
- Use the canonical section order in every `SKILL.md`.
- Keep names lowercase, hyphenated, stable, and reusable.

## Required `SKILL.md` Sections

Every skill must include:

1. Purpose
2. When To Use
3. Inputs
4. Process
5. Outputs
6. Guardrails
7. Verification
8. Escalation

## Responsibility Rule

Each skill should have one primary responsibility. If a skill starts combining concerns across intake, routing, execution, verification, or documentation, split it into smaller skills aligned to the canonical layer model.

## Scope Rules

- Keep base skills technology-agnostic.
- Do not embed framework-specific, vendor-specific, or project-specific assumptions into the base layer.
- Prefer concise instructions over long narrative explanations.
- Add supporting templates or references only when they are genuinely reusable.

## Authoring Guidance

- Write instructions that another Codex instance can follow without extra interpretation.
- Separate facts, assumptions, and guardrails clearly.
- Prefer practical steps and concrete outputs over abstract principles.
- Keep skills composable so orchestration can combine them cleanly.

## Maintenance Rules

- Update the manifest and index whenever a skill is added, renamed, deprecated, or retired.
- Keep documentation aligned with the actual repository structure.
- Do not let examples become alternate sources of truth for the canonical base layer.
