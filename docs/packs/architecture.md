# Pack Architecture

## Purpose

Packs are the repository's second organizational axis. They let specialized skill content grow without changing the canonical base skills under `.codex/skills/`.

## Canonical Terms

Use these terms consistently:

- `base skills`
  - `.codex/skills/`
- `direct pack`
  - `packs/<pack-name>/`
- `solution group`
  - `packs/<group>/`
- `leaf pack`
  - `packs/<group>/<pack-name>/`

## Two-Axis Model

The repository uses two complementary axes:

1. responsibility layer
   - `orchestration`
   - `guardrails`
   - `atomic`
2. pack organization
   - direct packs
   - solution groups
   - leaf packs

Layer and pack are not the same thing:

- layer describes what responsibility a skill performs
- pack placement describes where specialized content belongs organizationally
- a leaf pack may contain orchestration, guardrails, and atomic skills
- pack placement never replaces layer classification

## Classification Rules

### When To Create A Direct Pack

Use a direct pack at `packs/<pack-name>/` when the pack:

- represents a cross-cutting capability
- represents a workflow
- is not naturally tied to a single solution group

Canonical example:

- `packs/skill-development/`

### When To Create A Solution Group And Leaf Pack

Use a solution group plus a leaf pack when the pack clearly belongs to a functional area such as:

- frontend
- backend
- platform
- ai
- data

Canonical examples:

- `packs/frontend/angular/`
- `packs/frontend/react/`
- `packs/backend/python/`
- `packs/backend/dotnet/`
- `packs/platform/devops/`

## Structure Rules

### Solution Group

A solution group is a lightweight organizational container.

It must:

- contain only `README.md`
- not contain `skills-manifest.md`
- not contain `skills-index.md`
- not be treated as a pack root

### Direct Pack And Leaf Pack

Every direct pack or leaf pack should contain:

- `README.md`
- `skills-manifest.md`
- `skills-index.md`

Optional directories may be added when the pack has real content:

```text
pack-root/
  README.md
  skills-manifest.md
  skills-index.md
  skills/
  examples/
  docs/
  rules/
```

## Boundaries

- packs are extensions, not canonical base content
- packs must not relabel, replace, or absorb canonical base skills
- base skills stay independent from packs
- direct packs and leaf packs maintain their own manifests, indexes, and supporting docs

## Current Canonical Examples

- direct pack: `packs/skill-development/`
- solution group: `packs/frontend/`
- leaf pack: `packs/frontend/angular/`
- leaf pack: `packs/frontend/react/`
- leaf pack: `packs/backend/python/`
- leaf pack: `packs/backend/dotnet/`
- leaf pack: `packs/platform/devops/`
