# Frontend Solution Group

This solution group organizes specialized packs for frontend ecosystems. It is a lightweight container, not a pack root.

## Included Leaf Packs

- `packs/frontend/angular/`
- `packs/frontend/react/`

## Relationship To The Layer Model

The `frontend` solution group organizes packs by functional area only. Any skills added inside its leaf packs still use the canonical responsibility layers:

- `orchestration`
- `guardrails`
- `atomic`

## Boundaries

- keep only `README.md` at the solution-group root
- place actual pack manifests and indexes inside each leaf pack
- do not treat the solution group itself as a replacement for canonical base skills
