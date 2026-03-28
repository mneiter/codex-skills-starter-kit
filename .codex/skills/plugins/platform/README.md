# Platform Plugin Group

This plugin group organizes specialized plugins for platform and operational ecosystems. It is a lightweight container, not a plugin root.

## Included Plugin Locations

- `.codex/skills/plugins/platform/devops/` as an actual plugin root

## Relationship To The Layer Model

The `platform` plugin group organizes reusable extensions by functional area only. Any future skills added inside its plugins still use the canonical responsibility layers:

- `orchestration`
- `guardrails`
- `atomic`

## Boundaries

- keep only `README.md` at the plugin-group root
- do not add `plugin-manifest.md` or `plugin-index.md` here
- do not treat the plugin group itself as a replacement for canonical base skills
- keep plugin catalogs and skills inside plugin roots such as `.codex/skills/plugins/platform/devops/`
