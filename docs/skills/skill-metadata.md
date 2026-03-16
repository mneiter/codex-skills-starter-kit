# Skill Metadata

## Purpose

This document defines the normalized metadata model for skills in `codex-skills-starter-kit`. The metadata contract is tooling-facing and is derived from the existing skill structure rather than from a breaking rewrite of every `SKILL.md`.

## Normalized Metadata Record

Every skill should normalize to this record:

```yaml
name: ci-verification
layer: atomic
purpose: Confirm whether a change passes the repository's available verification steps.
triggers:
  - Run relevant repository validation steps and interpret the results.
  - implementation is complete
  - a change needs validation evidence
inputs:
  - the set of relevant validation commands or checks
  - the current repository state
outputs:
  - a concise validation summary
  - command results or evidence references
dependencies: []
verification:
  - The chosen checks match the scope of the change.
  - Results are accurately reported.
```

## Canonical Fields

| Field | Type | Meaning | Source |
| --- | --- | --- | --- |
| `name` | string | Stable skill identifier. | Frontmatter `name` |
| `layer` | string | Responsibility classification. | Manifest entry, or path-derived fallback for canonical base skills |
| `purpose` | string | Single-sentence summary of the skill's job. | `# Purpose` |
| `triggers` | list of strings | The user-intent signals that should activate the skill. | Frontmatter `description` plus `# When To Use` |
| `inputs` | list of strings | Required context, artifacts, or constraints. | `# Inputs` |
| `outputs` | list of strings | Expected results, artifacts, or decisions. | `# Outputs` |
| `dependencies` | list of strings | Non-obvious tools, skills, or reusable resources the skill relies on. | Explicit `Dependencies:` notes in `# Inputs`, or `[]` |
| `verification` | list of strings | How to confirm the skill result is complete and within scope. | `# Verification` |

## Canonical Layer Values

Use the repository's existing layer tokens exactly:

- `atomic`
- `guardrails`
- `orchestration`

The repository uses `guardrails` as the canonical token because it matches the current folder structure and base manifests.

## Compatibility Model

The current standard is intentionally incremental:

- `SKILL.md` frontmatter stays limited to `name` and `description`
- the required section order stays unchanged
- existing skills remain valid as long as the normalized fields can be derived
- pack skills use the same normalized metadata model as canonical base skills

## Authoring Guidance

To keep normalized metadata accurate:

- keep the first paragraph of `Purpose` concise and specific
- use list-shaped content in `When To Use`, `Inputs`, `Outputs`, and `Verification`
- add one `Inputs` bullet that starts with `Dependencies:` when the skill relies on named tools, skills, or shared resources
- keep the description and `When To Use` complementary instead of duplicating the same sentence

## Example Dependency Note

When dependencies exist, express them plainly inside `Inputs`:

```md
- Dependencies: shared-boundary-guardrails, scripts/validate-skills
```

If no dependencies need to be called out, the normalized metadata should use `[]`.
