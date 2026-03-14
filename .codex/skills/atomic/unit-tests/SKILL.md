---
name: unit-tests
description: Add or improve focused automated tests around isolated behavior. Use when a change needs regression protection, a defect should be reproduced, or a small stable unit of logic needs clearer verification coverage.
---

# Purpose

Create or improve small, focused tests that protect isolated behavior. Strengthen confidence without turning the test task into a broader integration or system design effort.

# When To Use

Use this skill when:

- a unit of logic lacks direct test coverage
- a bug should be reproduced with a targeted test
- a change needs regression protection
- the repository already supports automated tests for isolated behavior

# Inputs

- the behavior to test
- the relevant code unit or boundary
- the expected outcomes
- the repository's existing testing patterns

# Process

1. Define the smallest stable behavior worth testing.
2. Match the existing test style used by the repository.
3. Add tests that cover success paths and meaningful edge cases in scope.
4. Keep setup small and focused on the target unit.
5. Run the relevant test verification and report the outcome.

# Outputs

- focused automated tests
- coverage for the targeted behavior
- evidence that the tests pass or a clear failure report
- any remaining gaps that are intentionally out of scope

# Guardrails

- Do not turn a unit-test task into broad integration coverage.
- Do not duplicate existing tests without increasing confidence.
- Keep test setup readable and proportionate to the behavior under test.
- Prefer stable assertions over fragile implementation-coupled checks.

# Verification

- The new or updated tests directly protect the intended behavior.
- The tests fit the repository's existing style.
- Relevant test execution confirms the result or reveals actionable failures.
- The scope remains focused on isolated behavior.

# Escalation

Escalate when:

- the behavior cannot be isolated cleanly
- the repository lacks a clear unit-test pattern
- the real verification need belongs to a broader test layer
