# causix-scenario-agent

The `ScenarioAgent` for the Causix analysis pipeline.

## Usage

```python
from causix_scenario_agent import ScenarioAgent

agent = ScenarioAgent(llm)  # llm: causix_core.reasoning.llm.LLMClient
```

Depends on [core](../../core) for the LLM client, schemas and prompts.

## Development

```bash
uv sync
uv run pytest
```

