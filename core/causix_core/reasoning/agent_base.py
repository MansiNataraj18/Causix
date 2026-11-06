"""Shared agent plumbing: the error type and tolerant JSON extraction."""
import json


class AgentError(Exception):
    """Raised when an agent cannot produce a valid result."""


def extract_json(text: str) -> dict:
    """Take the outermost {...} block, so ```json fences or stray text don't break parsing."""
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end < start:
        raise AgentError("LLM response did not contain a JSON object")
    try:
        return json.loads(text[start:end + 1])
    except json.JSONDecodeError as exc:
        raise AgentError(f"LLM returned invalid JSON: {exc}") from exc
