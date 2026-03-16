# Evaluation Patterns

## Purpose

Use this reference when deciding how deeply to evaluate a skill.

## Lightweight Review

Use lightweight review first when:

- the skill is new
- the expected behavior is easy to inspect manually
- the main question is whether the description and scope make sense

A good lightweight review includes:

- 2-3 realistic prompts
- expected outcomes in plain language
- notes on whether the skill should or should not trigger
- one explicit decision about the next revision step

## Structured Evaluation

Use structured evaluation when:

- the skill handles objective tasks
- repeated regressions or weak behavior appear
- several revisions need comparison

Structured evaluation usually adds:

- clearly stated expectations
- prompt sets that reflect realistic user requests
- review notes about weak or missing assertions

## Comparison Review

Use comparison review when:

- two drafts compete
- one description revision must be judged against another
- a skill output is subjective enough that plain assertions are incomplete

Comparison works best when:

- the task and expected qualities are stated clearly
- the reviewer notes both strengths and weaknesses
- the result leads to a concrete decision rather than a vague preference

## Common Failure Signals

- the skill triggers in too many unrelated situations
- the skill fails to trigger on obvious matching requests
- the output looks superficially correct but misses the real intent
- the skill keeps growing because missing scope boundaries are being patched with more content
