# Codex Agent Rules

## Purpose

These rules define how Codex should operate in a downstream repository that adopts this starter kit.

## Working Style

- Start by understanding the affected area before editing.
- Prefer focused changes over broad speculative refactors.
- Use the repository's existing conventions unless the task explicitly requires change.

## Change Safety

- Do not rewrite unrelated files.
- Keep new abstractions justified and reviewable.
- Preserve existing behavior outside the requested scope.

## Documentation Expectations

- Update repository documentation when workflows, architecture, or developer expectations change.
- Keep documentation practical and repository-specific.
- Keep local manifests and indexes aligned with the actual skill set.

## Validation Expectations

- Run the relevant repository validation commands when possible.
- Report any command that could not be run.
- Distinguish verified results from assumptions.

## Skill Extension Rules

- Keep copied base skills generic.
- Add reusable extensions under `.codex/skills/plugins/`.
- Add repository-specific skills under `.codex/skills/project/`.
- Prefer small composable skills over large multi-purpose skills.
