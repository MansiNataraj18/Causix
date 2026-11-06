# Causix

Root-cause analysis, impact analysis and fix recommendation for code issues, built from small
single-purpose agents on a shared core.

```
core/                    shared engines + reasoning contracts      (package: causix_core)
agents/
  issue/                 raw report -> structured issue            (causix_issue_agent)
  rca/                   root cause analysis                       (causix_rca_agent)
  impact/                blast-radius explanation                  (causix_impact_agent)
  fix/                   fix + regression test recommendation      (causix_fix_agent)
  scenario/              validation scenario generation            (causix_scenario_agent)
  documentation/         documentation / lessons report            (causix_documentation_agent)
orchestrator/            FastAPI service, pipeline orchestrator, Aetherion entrypoint
```

Dependency direction: `orchestrator -> agents -> core`. Agents never depend on each other.

## Development

This is a [uv workspace](https://docs.astral.sh/uv/concepts/projects/workspaces/); one sync
installs every member in editable mode.

```bash
uv sync --all-packages
uv run --package causix-core pytest core
uv run --package causix-rca-agent pytest agents/rca
uv run --package causix-orchestrator pytest orchestrator
```

Each member is tested from its own directory (`cd core && uv run pytest`). Each has its own README.
