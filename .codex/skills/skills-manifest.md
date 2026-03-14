# Skills Manifest

This manifest is the canonical registry of base skills in `codex-skills-starter-kit`.

## Status Values

- `active`: approved and recommended for normal use
- `experimental`: available for trial use but not yet stable
- `deprecated`: still present but scheduled for replacement or removal
- `retired`: kept only for historical reference and not recommended for use

## Base Skills

| Skill | Layer | Status | Path | Purpose |
| --- | --- | --- | --- | --- |
| task-intake-supervisor | orchestration | active | `.codex/skills/orchestration/task-intake-supervisor/SKILL.md` | Normalize new requests into a clear task frame with scope, risks, and handoff guidance. |
| skill-router | orchestration | active | `.codex/skills/orchestration/skill-router/SKILL.md` | Select the right skills, order them, and define how work should move between them. |
| execution-memory-loop | guardrails | active | `.codex/skills/guardrails/execution-memory-loop/SKILL.md` | Maintain checkpoints, working memory, and next-step clarity during longer tasks. |
| review-and-repair-loop | guardrails | active | `.codex/skills/guardrails/review-and-repair-loop/SKILL.md` | Recheck work, find defects, repair them, and verify the result before closing. |
| shared-boundary-guardrails | guardrails | active | `.codex/skills/guardrails/shared-boundary-guardrails/SKILL.md` | Enforce shared boundaries for safe, generic, and bounded execution. |
| ci-verification | atomic | active | `.codex/skills/atomic/ci-verification/SKILL.md` | Run and interpret repository validation steps to confirm change safety. |
| generate-pull-request | atomic | active | `.codex/skills/atomic/generate-pull-request/SKILL.md` | Draft a concise pull request narrative from implemented changes and evidence. |
| refactor-feature | atomic | active | `.codex/skills/atomic/refactor-feature/SKILL.md` | Reshape an existing feature without expanding scope or changing intended behavior. |
| unit-tests | atomic | active | `.codex/skills/atomic/unit-tests/SKILL.md` | Add or improve focused automated tests around isolated behavior. |
