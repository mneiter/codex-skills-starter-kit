# Backend Plugin Group

This plugin group organizes specialized plugins for backend ecosystems. It is a lightweight container, not a plugin root.

## Included Plugin Locations

- `.codex/skills/plugins/backend/python/`
- `.codex/skills/plugins/backend/dotnet/`

## Relationship To The Layer Model

The `backend` plugin group organizes reusable extensions by functional area only. Any future skills added inside its plugins still use the canonical responsibility layers:

- `orchestration`
- `guardrails`
- `atomic`

## Boundaries

- keep only `README.md` at the plugin-group root
- do not add `plugin-manifest.md` or `plugin-index.md` here
- do not treat the plugin group itself as a replacement for canonical base skills
