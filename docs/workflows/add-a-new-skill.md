# Add A New Skill

## Goal

Use this workflow when extending a repository that already uses the starter kit.

## Step 1: Decide Whether A New Skill Is Needed

Add a new skill only if the work cannot be cleanly handled by the current catalog. Prefer updating documentation or routing before creating overlapping skills.

## Step 2: Choose The Right Layer

- use `orchestration` for intake, routing, sequencing, or handoff
- use `guardrails` for boundaries, review loops, or persistent execution discipline
- use `atomic` for one focused repeatable task

If the skill does not fit the base layer cleanly, place it in a project-local area or in a separate pack. Do not widen the canonical base layer just because a workflow is useful in one class of projects.

## Step 3: Author The Skill

- copy the canonical template from `templates/skill-template/SKILL.md`
- keep one primary responsibility
- write the description first in user-intent language so neighboring skills stay distinguishable
- write clear inputs, process steps, outputs, guardrails, verification, and escalation rules
- keep the frontmatter limited to `name` and `description`
- decide whether bundled `scripts/`, `references/`, or `assets/` are actually needed before adding them

## Step 4: Plan Evaluation

- choose 2-3 realistic prompts if the skill has objective behavior
- write expected outcomes in plain language before building a larger evaluation loop
- decide whether the skill needs simple review, structured assertions, or only qualitative feedback
- revise the description or scope before adding more resources if trigger quality is the main problem

## Step 5: Register The Skill

- add the skill to the manifest with the correct layer, status, path, and purpose
- add the skill to the index with a short purpose and when-to-use summary
- update any relevant documentation or onboarding material

## Step 6: Verify Boundaries

- confirm the skill does not pollute the base layer with project-specific or technology-specific assumptions
- confirm the skill is not duplicating a neighboring skill
- confirm the skill remains small enough to compose with others
- confirm it belongs in the base layer rather than in a pack or project-local area

## Step 7: Maintain Over Time

- update status as the skill matures
- retire or split skills that become too broad
- keep the catalog accurate so routing decisions stay simple
