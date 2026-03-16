# Evaluate A Skill

## Goal

Use this workflow to check whether a skill is triggering correctly, staying within scope, and producing useful outputs.

## Start With The Skill Type

Different skills need different evaluation depth.

- objective skills usually benefit from realistic prompts and concrete expected outcomes
- subjective skills usually benefit from review criteria and comparison rather than strict pass/fail assertions
- mixed skills often need a small practical check first, then deeper evaluation only if they still underperform

## Minimum Viable Evaluation

Use this default workflow before building anything more elaborate:

1. write 2-3 realistic prompts that a real user would likely use
2. define the expected outcome for each prompt in plain language
3. run the skill on those prompts
4. review whether the skill triggered correctly and produced the intended result
5. record one decision:
   - keep as is
   - revise description
   - add resources
   - split skill
   - move to pack

This lightweight path is often enough to catch weak descriptions, scope overlap, or missing guidance.

## Realistic Prompt Selection

- choose prompts that sound like real user requests
- include at least one prompt that should trigger clearly
- include at least one nearby prompt that should not trigger when overlap is a known risk
- avoid toy prompts that prove little about real behavior

## Expected Outcomes

Write expected outcomes in plain language before reviewing results.

- what should the skill help produce
- what should remain out of scope
- what would count as a clearly wrong trigger
- what would count as a clearly weak result

## Review Criteria

Check these dimensions:

- trigger quality: did the skill activate when it should
- boundary quality: did it stay inactive when it should not apply
- output quality: did the result match the intended outcome
- scope discipline: did the skill stay within one responsibility

## Assertion Quality

If you add structured assertions later, make them discriminating.

- avoid assertions that pass on superficial output
- prefer assertions tied to meaningful task completion
- note missing coverage when an important outcome is not being checked

## Manual Review And Comparison

For subjective or mixed skills, a short structured review can be enough.

- compare the result to the intended behavior
- note whether the description, process, or resources are the main weakness
- use blind comparison only when it will clarify ambiguous quality differences

## Typical Outcomes

- revise the description when triggering is wrong but the workflow is sound
- add resources when the workflow is right but execution depth is missing
- split the skill when it is mixing concerns
- move the skill to a pack when it is useful but too specialized for the base layer
