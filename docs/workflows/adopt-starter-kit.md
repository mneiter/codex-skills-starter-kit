# Adopt The Starter Kit

## Goal

Use this workflow when copying `codex-skills-starter-kit` into a new repository.

## Adoption Steps

1. Copy the starter-kit structure into the target repository.
2. Keep the canonical base skills unchanged on first adoption.
3. Replace the downstream `AGENTS.md` template content with repository-specific rules.
4. Fill in the onboarding document with repository purpose, constraints, validation paths, and architecture notes.
5. Review the root manifest and index so they reflect the skills that now exist in the repository.
6. Add project skills only after the base layer is in place.

## Recommended First Customizations

- repository-specific `AGENTS.md`
- local onboarding documentation
- project skill entries in the root manifest and index

## Extension Guidance

- Put project-specific skills under `.codex/skills/project/` when they are not broadly reusable.
- Use `.codex/skills/plugins/<plugin-name>/` for reusable cross-cutting extensions such as `.codex/skills/plugins/skill-development/`.
- Use `.codex/skills/plugins/<group>/<plugin-name>/` when the plugin clearly belongs to a plugin group such as `.codex/skills/plugins/frontend/angular/`.
- Keep plugin groups lightweight and place `plugin-manifest.md` and `plugin-index.md` only inside actual plugin roots.
- Preserve the meaning and names of canonical base skills.

## Anti-Patterns

- editing base skills to carry project-specific knowledge
- mixing local workflow rules into shared generic skills
- treating a plugin group as a plugin root
- skipping manifest and index updates after adding skills
