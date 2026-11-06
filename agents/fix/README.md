# causix-fix-agent

The `FixAgent` for the Causix analysis pipeline.

## Usage

```python
from causix_fix_agent import FixAgent

agent = FixAgent(llm)  # llm: causix_core.reasoning.llm.LLMClient
```

Depends on [core](../../core) for the LLM client, schemas and prompts.

## Development

```bash
uv sync
uv run pytest
```

