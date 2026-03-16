# Plugins

The `.codex/skills/plugins/` area holds reusable extensions that do not belong in the canonical base layer.

## What Belongs Here

- actual plugins with reusable skills
- plugin groups that organize related plugin locations
- reusable references, templates, and other support material owned by actual plugins

## Structure Rules

- use `.codex/skills/plugins/<plugin-name>/` for a cross-cutting actual plugin such as `skill-development`
- use `.codex/skills/plugins/<group>/` for a plugin group container
- use `.codex/skills/plugins/<group>/<plugin-name>/` for a grouped plugin location
- keep `plugin-manifest.md` and `plugin-index.md` only inside actual plugin roots that contain skills
- keep plugin groups and empty plugin scaffolds out of the root skill registries
