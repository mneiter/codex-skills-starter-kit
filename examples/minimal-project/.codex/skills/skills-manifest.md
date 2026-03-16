# Minimal Project Skills Manifest

This example manifest shows how an adopted repository can register local additions without redefining the canonical base layer.

## Status Values

- `active`: approved and recommended for normal use
- `experimental`: available for trial use but not yet stable
- `deprecated`: still present but scheduled for replacement or removal
- `retired`: kept only for historical reference and not recommended for use

## Base Layer Note

In a real adopted repository, keep the canonical base manifest copied from the starter kit. This example omits the base entries to stay focused on local extensions.

## Optional Pack Note

If the repository attaches an optional pack under `packs/`, keep that pack's entries in the pack's own manifest and docs. Do not fold optional pack skills into the canonical base manifest.

## Project-Local Skills

| Skill | Layer | Status | Path | Purpose |
| --- | --- | --- | --- | --- |
| project-context | project-local | active | `.codex/skills/project-local/project-context/SKILL.md` | Capture repository-specific goals, constraints, and terminology that should not live in the canonical base layer. |
