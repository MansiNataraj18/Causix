# causix-issue-agent

The `IssueAgent` for the Causix analysis pipeline.

## Usage

```python
from causix_issue_agent import IssueAgent

agent = IssueAgent(llm)  # llm: causix_core.reasoning.llm.LLMClient
```

Depends on [core](../../core) for the LLM client, schemas and prompts.

## Development

```bash
uv sync
uv run pytest
```

