# causix-orchestrator

Runs the Causix pipeline: FastAPI service, orchestrator and Aetherion agent entrypoint.

Chains `causix-issue-agent` -> `causix-rca-agent` -> `causix-impact-agent` -> `causix-fix-agent` -> `causix-scenario-agent` -> `causix-documentation-agent`, using engines from `causix-core`.

## Development

```bash
uv sync
uv run pytest
uv run uvicorn src.api.main:app --reload
```

Copy `.env.template` to `.env` and `docker compose up -d` for a local Neo4j.

