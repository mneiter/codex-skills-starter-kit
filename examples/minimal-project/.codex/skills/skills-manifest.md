# Minimal Project Skills Manifest

This example manifest shows how an adopted repository can register local additions without redefining the canonical base layer. In a real adopted repository, this remains the global skill registry.

## Status Values

- `active`: approved and recommended for normal use
- `experimental`: available for trial use but not yet stable
- `deprecated`: still present but scheduled for replacement or removal
- `retired`: kept only for historical reference and not recommended for use

## Base Layer Note

In a real adopted repository, keep the canonical base manifest copied from the starter kit. This example omits the base entries to stay focused on local extensions.

## Optional Plugin Note

If the repository attaches an actual plugin under `.codex/skills/plugins/`, keep that plugin's entries in the plugin's own manifest and docs as well as in the root global manifest. Do not register plugin groups or empty plugin scaffolds.

## Skills

| Skill | Scope | Layer | Status | Path | Purpose |
| --- | --- | --- | --- | --- | --- |
| project-context | project | orchestration | active | `.codex/skills/project/project-context/SKILL.md` | Capture repository-specific goals, constraints, and terminology that should not live in the canonical base layer. |
