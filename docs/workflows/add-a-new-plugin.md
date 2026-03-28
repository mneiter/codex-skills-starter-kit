# Add A New Plugin

## Goal

Use this workflow when extending the repository with a new reusable plugin.

## Step 1: Choose The Right Plugin Placement

Create a top-level plugin at `.codex/skills/plugins/<plugin-name>/` when the plugin:

- represents a cross-cutting capability
- represents a workflow
- is not naturally tied to one plugin group

Canonical example:

- `.codex/skills/plugins/skill-development/`

Create a grouped plugin at `.codex/skills/plugins/<group>/<plugin-name>/` when the plugin clearly belongs to a functional area such as:

- frontend
- backend
- platform
- ai
- data

Canonical examples:

- `.codex/skills/plugins/frontend/angular/`
- `.codex/skills/plugins/frontend/react/`
- `.codex/skills/plugins/backend/python/`
- `.codex/skills/plugins/backend/dotnet/`
- `.codex/skills/plugins/platform/data/`
- `.codex/skills/plugins/platform/devops/`

## Step 2: Create A Plugin Group When Needed

If the plugin group does not exist yet:

- create `.codex/skills/plugins/<group>/`
- add only `README.md` at the plugin-group root
- do not add `plugin-manifest.md` or `plugin-index.md` at the plugin-group root

## Step 3: Create The Plugin Root

For an actual plugin root with real skills, create:

- `README.md`
- `plugin-manifest.md`
- `plugin-index.md`
- `skills/`

Optional directories may be added only when the plugin has real content:

- `examples/`
- `docs/`
- `rules/`
- `references/`
- `templates/`

If the plugin is only a future placeholder with no real skills yet, keep it as a README-only scaffold and do not register it globally.

## Step 4: Keep The Layer Model Independent

- do not treat plugin placement as a replacement for layer classification
- any skill added to a plugin still uses `orchestration`, `guardrails`, or `atomic`
- do not modify canonical base skills just to fit a plugin

## Step 5: Validate

- run `scripts/validate-skills`
- confirm the plugin group is treated only as a container
- confirm the actual plugin manifest and index match the real skill folders
- confirm duplicate skill names were not introduced
