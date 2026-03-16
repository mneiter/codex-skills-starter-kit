# Codex Agent Rules

## Purpose

These rules define how Codex should operate when maintaining this starter-kit repository.

## Base Kit Boundaries

- Keep the canonical base kit technology-agnostic.
- Add new base skills only when they are reusable across many projects and do not depend on a specific stack, runtime, framework, vendor, or deployment model.
- Do not place plugin or project-specific skills inside `.codex/skills/base/orchestration`, `.codex/skills/base/guardrails`, or `.codex/skills/base/atomic`.
- Treat `.codex/skills/plugins/` as reusable extension space that must remain outside the canonical base layer.
- Treat `.codex/skills/project/` as repository-local space that must remain outside the reusable base layer.
- Use the canonical terms consistently: `base skills`, `plugin`, `plugin group`, and `project skills`.
- Keep `.codex/skills/plugins/<group>/` lightweight as a plugin group with only `README.md`.
- Keep `plugin-manifest.md` and `plugin-index.md` only inside actual plugin roots that contain skills.

## Repository Consistency

- Keep `README.md`, `STARTER_KIT_MANIFEST.md`, `.codex/skills/skills-manifest.md`, and `.codex/skills/skills-index.md` aligned with the actual skill set.
- When adding, renaming, or retiring a skill, update the manifest, index, and relevant docs in the same change.
- Keep examples minimal and illustrative; they should show adoption patterns, not duplicate the full starter kit.

## Authoring Expectations

- Keep all content in English.
- Preserve the required `SKILL.md` structure for base skills and templates.
- Keep names lowercase, stable, and reusable.
- Prefer focused, composable skills over broad skills that mix concerns.

## Change Safety

- Avoid adding repository clutter that is not part of the canonical starter kit.
- Do not introduce technology-specific guidance into base-layer skills.
- Do not rewrite existing documents just for style; make targeted changes that preserve intent.

## Validation Expectations

Before closing work, verify:

- required folders and files exist
- every base skill contains `SKILL.md`
- each skill frontmatter is valid and contains only `name` and `description`
- manifests and indexes reflect the real skill set
- the base kit remains technology-agnostic
