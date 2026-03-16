# Skill Validation

## Command

Run the repository validator from the repository root:

```bash
scripts/validate-skills
```

## What The Validator Checks

The validator confirms repository consistency for both canonical base skills and pack skills.

It checks:

- `.codex/skills/` exists
- every discovered skill folder contains `SKILL.md`
- each skill has `name` and `description` frontmatter
- normalized metadata can be derived for every discovered skill
- each derived `layer` value is valid
- duplicate skill names do not exist across base and packs
- the canonical base manifest and index match the real base skill folders
- every populated pack has its own manifest and index
- each populated pack manifest and index match the real pack skill folders

## Exit Behavior

- `INFO` lines describe normal discovery or empty pack scaffolds
- `WARN` lines describe non-blocking issues
- `ERROR` lines describe blocking validation failures
- exit code `0` means the repository passed validation
- exit code `1` means one or more blocking errors were found

## Sample Clean Output

```text
INFO: discovered 9 canonical base skills
INFO: pack angular has no skills yet
INFO: pack devops has no skills yet
INFO: pack python has no skills yet
INFO: pack react has no skills yet
INFO: validated 3 skills in pack skill-development
INFO: validation passed with 12 skills checked, 0 errors, 0 warnings
```

## When To Run It

Run the validator whenever you:

- add, remove, or rename a skill
- update a skill manifest or index
- change pack structure
- adjust the skill metadata rules or validation tooling
