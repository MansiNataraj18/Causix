# causix-core

Shared library used by every Causix agent.

| Package | Purpose |
|---|---|
| `causix_core.reasoning` | LLM client, schemas, prompts, retrieval, report, `agent_base` |
| `causix_core.parser`, `git_history`, `repo_ingestion`, `repository` | Reading a repository |
| `causix_core.graph` | Neo4j code graph |
| `causix_core.rca`, `fix_localization`, `impact_analysis`, `architecture` | Analysis engines |
| `causix_core.validation` | Scenario validation runs |

## Development

```bash
uv sync
uv run pytest
```

