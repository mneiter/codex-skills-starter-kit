# Minimal Adopted Project Example

This example shows the shape of a repository after it adopts the starter kit and then adds a small project skill.

## What This Example Includes

- a repository-level `AGENTS.md`
- a project onboarding document
- a root skill manifest and index
- one project skill: `project-context`

## What This Example Intentionally Omits

The canonical base skills are assumed to have been copied into the real repository root from this starter kit. They are omitted here for brevity so the example stays focused on adoption-specific companion files rather than duplicating the full base layer.

## Adoption Pattern Illustrated

1. copy the canonical base layer from the starter kit
2. customize repository guidance and onboarding
3. register local additions in the root manifest and index
4. add project skills under `.codex/skills/project/`

## Optional Plugin Note

An adopting repository may also attach a reusable plugin under `.codex/skills/plugins/`, such as `.codex/skills/plugins/skill-development/`, when it needs extra guidance without folding that guidance into the canonical base layer. Actual plugins should keep their own plugin manifest and plugin index in addition to being registered in the root catalogs.
