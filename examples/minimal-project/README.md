# Minimal Adopted Project Example

This example shows the shape of a repository after it adopts the starter kit and then adds a small project-local skill.

## What This Example Includes

- a repository-level `AGENTS.md`
- a project onboarding document
- a local skill manifest and index
- one project-local skill: `project-context`

## What This Example Intentionally Omits

The canonical base skills are assumed to have been copied into the real repository root from this starter kit. They are omitted here for brevity so the example stays focused on adoption-specific companion files rather than duplicating the full base layer.

## Adoption Pattern Illustrated

1. copy the canonical base layer from the starter kit
2. customize repository guidance and onboarding
3. register local additions in the manifest and index
4. add project-local skills outside the canonical base folders

## Optional Pack Note

An adopting repository may also attach an optional extension under `packs/`, such as `packs/skill-development/`, when it needs extra guidance without folding that guidance into the canonical base layer. Pack skills should keep their own pack manifest and docs instead of being merged into the canonical base manifest.
