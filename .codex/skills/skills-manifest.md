# Skills Manifest

This manifest is the global skill registry for `codex-skills-starter-kit`. It is the single discovery surface for all actual skills that live under `.codex/skills/`.

## Status Values

- `active`: approved and recommended for normal use
- `experimental`: available for trial use but not yet stable
- `deprecated`: still present but scheduled for replacement or removal
- `retired`: kept only for historical reference and not recommended for use

## Skills

| Skill | Scope | Layer | Status | Path | Purpose |
| --- | --- | --- | --- | --- | --- |
| task-intake-supervisor | base | orchestration | active | `.codex/skills/base/orchestration/task-intake-supervisor/SKILL.md` | Normalize new requests into a clear task frame with scope, risks, and handoff guidance. |
| skill-router | base | orchestration | active | `.codex/skills/base/orchestration/skill-router/SKILL.md` | Select the right skills, order them, and define how work should move between them. |
| execution-memory-loop | base | guardrails | active | `.codex/skills/base/guardrails/execution-memory-loop/SKILL.md` | Maintain checkpoints, working memory, and next-step clarity during longer tasks. |
| review-and-repair-loop | base | guardrails | active | `.codex/skills/base/guardrails/review-and-repair-loop/SKILL.md` | Recheck work, find defects, repair them, and verify the result before closing. |
| shared-boundary-guardrails | base | guardrails | active | `.codex/skills/base/guardrails/shared-boundary-guardrails/SKILL.md` | Enforce shared boundaries for safe, generic, and bounded execution. |
| ci-verification | base | atomic | active | `.codex/skills/base/atomic/ci-verification/SKILL.md` | Run and interpret repository validation steps to confirm change safety. |
| generate-pull-request | base | atomic | active | `.codex/skills/base/atomic/generate-pull-request/SKILL.md` | Draft a concise pull request narrative from implemented changes and evidence. |
| refactor-feature | base | atomic | active | `.codex/skills/base/atomic/refactor-feature/SKILL.md` | Reshape an existing feature without expanding scope or changing intended behavior. |
| unit-tests | base | atomic | active | `.codex/skills/base/atomic/unit-tests/SKILL.md` | Add or improve focused automated tests around isolated behavior. |
| author-skill | plugin | atomic | active | `.codex/skills/plugins/skill-development/skills/author-skill/SKILL.md` | Guide the drafting of a new skill with clear scope, structure, and resource decisions. |
| evaluate-skill | plugin | guardrails | active | `.codex/skills/plugins/skill-development/skills/evaluate-skill/SKILL.md` | Review whether a skill triggers correctly, stays within scope, and produces useful outputs. |
| optimize-skill-description | plugin | atomic | active | `.codex/skills/plugins/skill-development/skills/optimize-skill-description/SKILL.md` | Improve a skill description so it better matches user intent and avoids false triggers. |
