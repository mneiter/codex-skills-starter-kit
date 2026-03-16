# Skill Description Writing

## Purpose

Use this guide when writing or revising the `description` field in `SKILL.md` frontmatter. The description is the primary trigger surface for a skill, so it should help Codex recognize when the skill is useful before the skill body is loaded.

## Core Principles

- Write for user intent, not only for implementation detail.
- Keep the wording distinctive so the skill does not blur into nearby skills.
- Prefer broad, reusable intent categories over long lists of narrow examples.
- Keep the description concise enough to stay readable and memorable.

## Trigger Phrase Guidance

Good descriptions include language that maps to the way a user would naturally ask for help.

- mention likely user phrases such as "review", "refactor", "validate", or "write tests" when those phrases genuinely align with the skill
- include neighboring terms that point to the same intent when they improve trigger quality
- avoid keyword stuffing; every phrase should reinforce the same core responsibility

## User-Intent Wording

Describe what the user is trying to achieve.

- stronger: "Use when the user needs to validate a change before review"
- weaker: "Runs commands and parses outputs"

Intent-focused wording works better because it generalizes across repositories, tools, and implementation details.

## Negative Boundaries

Descriptions should also make clear when a skill should not trigger.

- mention adjacent concerns that belong to a different skill when confusion is likely
- avoid descriptions so broad that they steal work from neighboring skills
- use negative boundaries to preserve one primary responsibility

Examples:

- `review-and-repair-loop` should not become the default implementation skill
- `unit-tests` should not imply broad integration or end-to-end test design
- `task-intake-supervisor` should not imply active implementation

## Writing Pattern

A reliable structure is:

1. state what the skill helps accomplish
2. state when to use it
3. state one or two boundary hints if overlap is likely

Example pattern:

`Use this skill when the user needs to improve automated test coverage for isolated behavior, reproduce a defect with focused tests, or protect a small stable unit against regressions. Do not use it for broad integration or system-level testing.`

## What To Avoid

- implementation-heavy descriptions that read like internal design notes
- very long lists of example prompts
- vague labels such as "handles many tasks"
- descriptions that overlap several unrelated concerns
- descriptions that require project-specific knowledge to understand

## Review Checklist

- Does the description state the user-facing goal clearly?
- Are likely trigger phrases present without turning into keyword stuffing?
- Is the scope distinct from neighboring skills?
- Does the description include a useful boundary when overlap is likely?
- Could the description still work in another repository without local context?
