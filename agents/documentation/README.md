# causix-documentation-agent

The `DocumentationAgent` for the Causix analysis pipeline.

## Usage

```python
from causix_documentation_agent import DocumentationAgent

agent = DocumentationAgent(llm)  # llm: causix_core.reasoning.llm.LLMClient
```

Depends on [core](../../core) for the LLM client, schemas and prompts.

## Development

```bash
uv sync
uv run pytest
```

