# Adopt The Starter Kit

## Goal

Use this workflow when copying `codex-skills-starter-kit` into a new repository.

## Adoption Steps

1. Copy the starter-kit structure into the target repository.
2. Keep the canonical base skills unchanged on first adoption.
3. Replace the downstream `AGENTS.md` template content with repository-specific rules.
4. Fill in the onboarding document with repository purpose, constraints, validation paths, and architecture notes.
5. Review the manifest and index so they reflect the skills that now exist in the repository.
6. Add project-local skills only after the base layer is in place.

## Recommended First Customizations

- repository-specific `AGENTS.md`
- local onboarding documentation
- project-local skill entries in the manifest and index

## Extension Guidance

- Put project-local skills outside the canonical base folders when they are not broadly reusable.
- Use a direct pack at `packs/<pack-name>/` for cross-cutting capabilities or workflows such as `packs/skill-development/`.
- Use a leaf pack at `packs/<group>/<pack-name>/` when the pack clearly belongs to a solution group such as `packs/frontend/angular/`.
- Keep solution groups lightweight and place manifests and indexes only inside direct packs and leaf packs.
- Preserve the meaning and names of canonical base skills.

## Anti-Patterns

- editing base skills to carry project-specific knowledge
- mixing local workflow rules into shared generic skills
- treating a solution group as a pack root
- skipping manifest and index updates after adding skills
