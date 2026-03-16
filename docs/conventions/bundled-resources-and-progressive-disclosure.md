# Bundled Resources And Progressive Disclosure

## Purpose

Use this guide when deciding whether a skill needs additional files beyond `SKILL.md`.

## Progressive Disclosure Model

Skills work best when information is layered:

1. `name` and `description` help Codex decide whether the skill should trigger
2. `SKILL.md` provides the core workflow and decision points
3. bundled resources provide deeper support only when needed

This model keeps the main skill body lean while still allowing specialized depth.

## When To Use `references/`

Use `references/` for supporting material that should be read on demand.

- variant-specific guidance
- detailed schemas or conventions
- long examples or deeper background
- domain details that are relevant only in some cases

Prefer references when the material is useful, but not required every time the skill triggers.

## When To Use `scripts/`

Use `scripts/` for deterministic or repetitive workflows that are better executed than rewritten.

- validation helpers
- packaging helpers
- repeatable transforms
- data extraction or reporting utilities

When a script is stable and self-explanatory from its interface, treat it as a black box and direct the user to run `--help` or equivalent usage guidance before reading source.

## When To Use `assets/`

Use `assets/` for reusable files that become part of the output or help bootstrap it.

- templates
- sample structures
- reusable examples
- starter artifacts that are copied or adapted

## Keep `SKILL.md` Lean

- keep the main body focused on the core workflow
- move deep or variant-specific material out when the body starts feeling overloaded
- point clearly to bundled resources so another Codex instance knows when to load them
- avoid duplicating the same information in both the skill body and bundled resources

## Variant Organization

If one skill supports several variants, organize the references by variant instead of mixing everything into one large body.

Example pattern:

```text
my-skill/
  SKILL.md
  references/
    variant-a.md
    variant-b.md
```

The main skill should explain when to consult each variant-specific file.

## What Not To Do

- do not add bundled folders preemptively when no real need exists
- do not hide core workflow steps inside deep reference chains
- do not place project-specific or vendor-specific resources inside reusable base skills
- do not let resource growth turn one skill into several overlapping responsibilities

## Review Questions

- Does the main skill body stay readable without the extra files?
- Does each added resource clearly reduce repetition or improve reliability?
- Is each resource reusable enough to justify its existence?
- Should the skill be split instead of adding more resources?
