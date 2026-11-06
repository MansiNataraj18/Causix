# causix-rca-agent

The `RCAAgent` for the Causix analysis pipeline.

## Usage

```python
from causix_rca_agent import RCAAgent

agent = RCAAgent(llm)  # llm: causix_core.reasoning.llm.LLMClient
```

Depends on [core](../../core) for the LLM client, schemas and prompts.

## Development

```bash
uv sync
uv run pytest
```

