# Plugin Architecture

## Purpose

Plugins are the reusable extension area under `.codex/skills/plugins/`. They let specialized skill content grow without changing the canonical base skills under `.codex/skills/base/`.

## Core Terms

Use these terms consistently:

- `base skills`
  - `.codex/skills/base/`
- `plugin`
  - `.codex/skills/plugins/<plugin-name>/`
  - or `.codex/skills/plugins/<group>/<plugin-name>/`
- `plugin group`
  - `.codex/skills/plugins/<group>/`
- `project skills`
  - `.codex/skills/project/`

## Responsibility And Scope

The repository keeps two separate ideas:

1. responsibility layer
   - `orchestration`
   - `guardrails`
   - `atomic`
2. skill scope
   - base skills
   - plugins
   - project skills

Layer describes what a skill does. Scope describes where it belongs. Plugins and project skills still use the same three responsibility layers as base skills.

## Plugin Group Rules

A plugin group is an organizational container only.

It must:

- contain only `README.md`
- not contain `plugin-manifest.md`
- not contain `plugin-index.md`
- not appear in the root skill registries
- not be treated as a plugin root by the validator

## Actual Plugin Rules

An actual plugin root is a directory that contains real skills.

It must contain:

- `README.md`
- `plugin-manifest.md`
- `plugin-index.md`
- `skills/`

Optional directories may be added when the plugin has supporting material:

```text
plugin-root/
  README.md
  plugin-manifest.md
  plugin-index.md
  skills/
  references/
  templates/
  docs/
  rules/
  examples/
```

## Empty Plugin Scaffolds

An empty plugin scaffold is a future plugin location with no actual skills yet.

It may contain:

- `README.md`

It must not contain:

- `plugin-manifest.md`
- `plugin-index.md`

Empty plugin scaffolds are valid structural placeholders, but they are not globally registered until they contain real skills.

## Placement Rules

Use a top-level plugin at `.codex/skills/plugins/<plugin-name>/` when the extension is cross-cutting or not naturally tied to one plugin group.

Canonical example:

- `.codex/skills/plugins/skill-development/`

Use a plugin group plus a grouped plugin path when the extension clearly belongs to a functional area.

Canonical examples:

- `.codex/skills/plugins/frontend/angular/`
- `.codex/skills/plugins/frontend/react/`
- `.codex/skills/plugins/backend/python/`
- `.codex/skills/plugins/backend/dotnet/`
- `.codex/skills/plugins/platform/devops/`

## Boundaries

- plugins are reusable extensions, not canonical base content
- plugins must not relabel, replace, or absorb canonical base skills
- the root `.codex/skills/skills-manifest.md` and `.codex/skills/skills-index.md` remain the single global discovery surface
- plugin-local catalogs supplement discovery inside an actual plugin, but they do not replace the root registries
