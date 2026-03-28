---
name: github-operations
description: Manage GitHub workflow state across repositories, pull requests, issues, reviews, and checks. Use when work needs GitHub-aware triage or GitHub-side lifecycle actions, while keeping verification, repair, refactoring, orchestration, and PR writeups in separate skills.
---

# Purpose

Manage GitHub workflow state without absorbing implementation or verification work. This skill inspects repository, issue, pull request, review, and check state, applies bounded GitHub-side actions when the request is explicit, and ends with a clear next GitHub step or handoff.

# When To Use

Use this skill when:

- the user wants a repository, issue, or pull request state summary
- a pull request appears blocked and the next GitHub-side step needs to be identified
- review feedback should be grouped into actionable clusters
- issue or pull request lifecycle state should be triaged, labeled, or organized
- check or workflow status should be summarized at a triage level before choosing the next step
- a GitHub-side metadata action is needed and both the target and requested action are explicit

# When Not To Use

Do not use this skill when:

- the task needs multi-skill sequencing or workflow design; use `skill-router`
- the task needs validation execution or test interpretation; use `ci-verification`
- the task needs a reviewer-facing pull request summary; use `generate-pull-request`
- the task needs code or content repair after findings or failed checks; use `review-and-repair-loop`
- the task is a behavior-preserving structural cleanup; use `refactor-feature`
- the task asks for GitHub Actions authoring, workflow editing, deep CI diagnosis, deployment, infrastructure execution, or local code changes

# Inputs

- the repository, checkout, or GitHub URL or identifier in scope
- the target GitHub artifact, such as a repository, pull request, issue, review thread, or check run
- the requested outcome or GitHub-side action
- any current state already known by the user, including blocked status, failing checks, or review feedback
- Dependencies: GitHub access plus the adjacent base skills `skill-router`, `ci-verification`, `generate-pull-request`, `review-and-repair-loop`, and `refactor-feature`

# Capabilities

- inspect repository, issue, pull request, review, and check state
- summarize why a pull request is blocked at a GitHub workflow level
- cluster review feedback into actionable change groups
- interpret status checks and workflow signals at a summary level
- identify the next GitHub-native action based on current repository state
- perform bounded GitHub-side metadata actions only when the target and action are unambiguous

# Process

1. Resolve the repository and target GitHub artifact.
2. Classify the request as state inspection, lifecycle triage, review clustering, blocked-state triage, or explicit GitHub-side metadata action.
3. Gather only the GitHub evidence needed to answer the request.
4. Keep the work GitHub-scoped: summarize state, identify blockers, or prepare the requested bounded action.
5. If the task crosses into implementation, verification, repair, refactoring, or pull request narrative work, hand off to the appropriate base skill.
6. Return the GitHub state summary, any action taken or proposed, and the next step.

# Outputs

- a concise GitHub state summary
- the current blocker, status, or review cluster relevant to the request
- any GitHub-side metadata action that was taken or explicitly prepared
- a recommended next GitHub-native step or an explicit handoff to another skill

# Boundaries

- `skill-router` chooses when several skills are needed; `github-operations` handles only the GitHub workflow slice once the task is in scope.
- `ci-verification` owns running checks and interpreting validation evidence; `github-operations` only summarizes GitHub-reported status.
- `generate-pull-request` owns reviewer-facing pull request narrative; `github-operations` may prepare context but does not write the summary.
- `review-and-repair-loop` owns repairing findings and re-verifying results; `github-operations` may surface the findings but does not fix them.
- `refactor-feature` owns behavior-preserving structural cleanup; `github-operations` may identify that need but does not perform it.

# Handoffs

- hand off to `skill-router` when the task mixes GitHub state work with other execution concerns
- hand off to `ci-verification` when implemented changes need validation evidence
- hand off to `generate-pull-request` when the diff is ready and reviewer-facing narrative is next
- hand off to `review-and-repair-loop` when findings require code or content repair
- hand off to `refactor-feature` when the next step is structural cleanup rather than GitHub workflow action

# Example Workflows

1. Pull request blocked by checks: summarize the blocking checks, note whether the blocker is review or status based, and recommend the next GitHub-side step or handoff.
2. Review feedback triage: cluster comments by file or behavior area and identify which clusters become implementation work.
3. Issue backlog triage: summarize issue state, group duplicates or stale items, and recommend the next lifecycle action.
4. Ready diff, unclear next step: confirm the GitHub state and hand off to `generate-pull-request` or `ci-verification` as appropriate.

# Guardrails

- Do not mutate GitHub state unless both the target and the requested action are explicit and unambiguous.
- Do not present GitHub check status as proof that the local change is correct or fully verified.
- Do not drift into GitHub Actions authoring, workflow editing, deep CI diagnosis, deployment, release, or infrastructure execution.
- Do not make local code changes, refactors, or repairs inside this skill.
- Ask or hand off instead of guessing when the target, requested action, or next owner is unclear.

# Verification

- The result stays inside GitHub workflow scope.
- Any blocker or next step is tied to observed GitHub state rather than assumption.
- Any GitHub-side action was bounded, explicit, and matched the stated target.
- Work that required verification, repair, refactoring, orchestration, or pull request narrative was handed off instead of absorbed here.

# Escalation

Escalate when:

- the repository or target GitHub artifact cannot be resolved
- GitHub access is unavailable or insufficient for the requested inspection or action
- the task requires more than one skill and routing materially affects the outcome
- the request turns into implementation, verification, repair, refactoring, CI diagnosis, or broader DevOps execution
