# Add A New Pack

## Goal

Use this workflow when extending the repository with a new pack structure.

## Step 1: Choose The Right Pack Form

Create a direct pack at `packs/<pack-name>/` when the pack:

- represents a cross-cutting capability
- represents a workflow
- is not naturally tied to one solution group

Canonical example:

- `packs/skill-development/`

Create a leaf pack at `packs/<group>/<pack-name>/` when the pack clearly belongs to a functional area such as:

- frontend
- backend
- platform
- ai
- data

Canonical examples:

- `packs/frontend/angular/`
- `packs/frontend/react/`
- `packs/backend/python/`
- `packs/backend/dotnet/`
- `packs/platform/devops/`

## Step 2: Create A Solution Group When Needed

If the solution group does not exist yet:

- create `packs/<group>/`
- add only `README.md` at the solution-group root
- do not add `skills-manifest.md` or `skills-index.md` at the solution-group root

## Step 3: Create The Pack Root

For a direct pack or leaf pack, create:

- `README.md`
- `skills-manifest.md`
- `skills-index.md`

Optional directories may be added only when the pack has real content:

- `skills/`
- `examples/`
- `docs/`
- `rules/`

## Step 4: Keep The Layer Model Independent

- do not treat pack placement as a replacement for layer classification
- any skill added to a direct pack or leaf pack still uses `orchestration`, `guardrails`, or `atomic`
- do not modify canonical base skills just to fit a pack

## Step 5: Validate

- run `scripts/validate-skills`
- confirm the solution group is treated only as a container
- confirm the direct pack or leaf pack manifest and index match the real skill folders
- confirm duplicate skill names were not introduced
