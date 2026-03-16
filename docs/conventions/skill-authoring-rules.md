# Skill Authoring Rules

## Core Rules

- Keep all content in English.
- Write `SKILL.md` frontmatter with only `name` and `description`.
- Keep the description clear about what the skill does and when it should be used.
- Write descriptions around user intent, not only around implementation details.
- Use the canonical section order in every `SKILL.md`.
- Keep names lowercase, hyphenated, stable, and reusable.

## Metadata Model

The repository standardizes skill metadata as a normalized record that is derived from each `SKILL.md` and its manifest entry. The current model does not require expanding trigger frontmatter beyond `name` and `description`.

The normalized fields are:

- `name`
- `layer`
- `purpose`
- `triggers`
- `inputs`
- `outputs`
- `dependencies`
- `verification`

Use the repository's canonical layer tokens exactly:

- `atomic`
- `guardrails`
- `orchestration`

The validator derives metadata from the existing skill structure:

- `name` from frontmatter
- `layer` from the manifest entry, or path-derived fallback for canonical base skills
- `purpose` from the `Purpose` section
- `triggers` from the frontmatter description and `When To Use`
- `inputs` from the `Inputs` section
- `outputs` from the `Outputs` section
- `dependencies` from explicit dependency notes in `Inputs`, or `[]` when none are stated
- `verification` from the `Verification` section

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
- Place reusable extensions in `.codex/skills/plugins/` instead of widening the canonical base layer.

## Progressive Disclosure Rules

- Keep `SKILL.md` focused on the core workflow and decision points.
- Use `references/` for detailed guidance that should be loaded only when needed.
- Use `scripts/` for deterministic or repetitive workflows that should be invoked rather than re-explained.
- Use `assets/` for reusable output materials such as templates or example artifacts.
- When variants exist, route to the smallest relevant reference instead of mixing all variants into one body.

## Description Rules

- Make the description distinctive enough to compete with neighboring skills.
- Mention trigger phrases or situations the user is likely to express.
- State negative boundaries when confusion with nearby skills is likely.
- Avoid overfitting the description into a long list of narrow examples.

## Evaluation Planning Rules

- Plan some form of evaluation before expanding a skill that handles objective tasks.
- Objective skills usually benefit from realistic prompts, expected outcomes, and simple verification notes.
- Subjective skills may rely more on structured review criteria than on pass/fail assertions.
- If repeated review shows overlap, weak triggering, or overloaded scope, revise the skill or split it.

## Authoring Guidance

- Write instructions that another Codex instance can follow without extra interpretation.
- Separate facts, assumptions, and guardrails clearly.
- Prefer practical steps and concrete outputs over abstract principles.
- Keep skills composable so orchestration can combine them cleanly.
- Prefer bundled resources only when they reduce repetition or improve reliability.
- Keep the first paragraph of `Purpose` concise so it can serve as clean metadata.
- Write `When To Use`, `Inputs`, `Outputs`, and `Verification` as compact lists whenever practical so metadata stays easy to extract.
- If the skill has non-obvious dependencies, add one `Inputs` bullet that begins with `Dependencies:`.

## Maintenance Rules

- Update the manifest and index whenever a skill is added, renamed, deprecated, or retired.
- Keep documentation aligned with the actual repository structure.
- Do not let examples become alternate sources of truth for the canonical base layer.
- Run `scripts/validate-skills` after changing skills, manifests, indexes, plugin structure, or project skill locations.
