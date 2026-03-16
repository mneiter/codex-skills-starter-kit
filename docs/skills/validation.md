# Skill Validation

## Command

Run the repository validator from the repository root:

```bash
scripts/validate-skills
```

## What The Validator Checks

The validator confirms repository consistency for:

- canonical base skills
- direct packs
- solution groups
- leaf packs

It checks:

- `.codex/skills/` exists
- every discovered skill folder contains `SKILL.md`
- each skill has `name` and `description` frontmatter
- normalized metadata can be derived for every discovered skill
- each derived `layer` value is valid
- duplicate skill names do not exist across base skills, direct packs, and leaf packs
- the canonical base manifest and index match the real base skill folders
- every direct pack has its own manifest and index
- every leaf pack has its own manifest and index
- each direct pack and leaf pack manifest/index matches the real skill folders

## Pack Discovery Model

The validator recognizes:

- direct pack: `packs/<pack-name>/`
- solution group: `packs/<group>/`
- leaf pack: `packs/<group>/<pack-name>/`

Validation rules:

- solution groups are lightweight containers and are not treated as pack roots
- empty solution groups are valid scaffolds
- empty direct packs are valid scaffolds
- empty leaf packs are valid scaffolds

## Exit Behavior

- `INFO` lines describe discovery and valid empty scaffolds
- `WARN` lines describe non-blocking issues
- `ERROR` lines describe blocking validation failures
- exit code `0` means the repository passed validation
- exit code `1` means one or more blocking errors were found

## Sample Clean Output

```text
INFO: discovered 9 canonical base skills
INFO: validated 3 skills in direct pack skill-development
INFO: discovered solution group backend
INFO: leaf pack backend/dotnet has no skills yet
INFO: leaf pack backend/python has no skills yet
INFO: discovered solution group frontend
INFO: leaf pack frontend/angular has no skills yet
INFO: leaf pack frontend/react has no skills yet
INFO: discovered solution group platform
INFO: leaf pack platform/devops has no skills yet
INFO: validation passed with 12 skills checked, 0 errors, 0 warnings
```

## When To Run It

Run the validator whenever you:

- add, remove, or rename a skill
- update a skill manifest or index
- create, move, or rename a direct pack, solution group, or leaf pack
- adjust the skill metadata rules or validation tooling
