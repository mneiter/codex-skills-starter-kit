# Skill Validation

## Command

Run the repository validator from the repository root:

```bash
scripts/validate-skills
```

## What The Validator Checks

The validator confirms repository consistency for:

- canonical base skills
- actual plugins
- plugin groups
- project skills

It checks:

- `.codex/skills/` exists
- `.codex/skills/base/` exists
- `.codex/skills/plugins/` exists
- `.codex/skills/project/` exists
- every discovered skill folder contains `SKILL.md`
- each skill has `name` and `description` frontmatter
- normalized metadata can be derived for every discovered skill
- each derived `layer` value is valid
- duplicate skill names do not exist across base skills, plugins, and project skills
- the root skill manifest and index match the real globally discoverable skills
- every actual plugin has its own `plugin-manifest.md` and `plugin-index.md`
- each actual plugin manifest and index matches the real skill folders
- plugin groups are lightweight containers and are not treated as plugin roots
- empty plugin scaffolds are valid placeholders
- no stale base paths remain at `.codex/skills/atomic`, `.codex/skills/guardrails`, or `.codex/skills/orchestration`
- no globally discoverable skill path points outside `.codex/skills/`

## Plugin Discovery Model

The validator recognizes:

- actual plugin: `.codex/skills/plugins/<plugin-name>/`
- plugin group: `.codex/skills/plugins/<group>/`
- grouped plugin path: `.codex/skills/plugins/<group>/<plugin-name>/`
- project skill: `.codex/skills/project/<skill-name>/SKILL.md`

Validation rules:

- plugin groups are lightweight containers and are not treated as plugin roots
- only actual plugins with real skills require `plugin-manifest.md` and `plugin-index.md`
- empty plugin scaffolds are valid when they contain only `README.md`
- only actual skills are registered in the root manifest and index

## Exit Behavior

- `INFO` lines describe discovery and valid empty scaffolds
- `WARN` lines describe non-blocking issues
- `ERROR` lines describe blocking validation failures
- exit code `0` means the repository passed validation
- exit code `1` means one or more blocking errors were found

## Sample Clean Output

```text
INFO: discovered 9 canonical base skills
INFO: validated 3 skills in plugin skill-development
INFO: discovered plugin group backend
INFO: empty plugin scaffold backend/dotnet
INFO: empty plugin scaffold backend/python
INFO: discovered plugin group frontend
INFO: empty plugin scaffold frontend/angular
INFO: empty plugin scaffold frontend/react
INFO: discovered plugin group platform
INFO: empty plugin scaffold platform/devops
INFO: validation passed with 12 skills checked, 0 errors, 0 warnings
```

## When To Run It

Run the validator whenever you:

- add, remove, or rename a skill
- update a skill manifest or index
- create, move, or rename a plugin or plugin group
- adjust the skill metadata rules or validation tooling
