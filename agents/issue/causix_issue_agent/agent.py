"""Issue Agent: turns a raw report into a structured IssueUnderstanding."""
from pydantic import ValidationError

from causix_core.reasoning.agent_base import AgentError, extract_json
from causix_core.reasoning.llm import LLMClient
from causix_core.reasoning.prompts import ISSUE_SYSTEM, build_issue_prompt
from causix_core.reasoning.schemas import IssueUnderstanding


class IssueAgent:
    def __init__(self, llm: LLMClient) -> None:
        self.llm = llm

    def run(self, issue: str, stack_trace: str | None = None, logs: str | None = None) -> IssueUnderstanding:
        raw = self.llm.complete(ISSUE_SYSTEM, build_issue_prompt(issue, stack_trace, logs))
        try:
            return IssueUnderstanding(**extract_json(raw))
        except ValidationError as exc:
            raise AgentError(f"LLM JSON did not match IssueUnderstanding: {exc}") from exc
