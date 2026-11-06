import json


from causix_scenario_agent import ScenarioAgent
from causix_core.reasoning.llm import FakeLLM
from causix_core.reasoning.schemas import FixRecommendation, IssueUnderstanding, RegressionTest

ISSUE = IssueUnderstanding(summary="Refund fails for customers without a payment profile")
FIX = FixRecommendation(
    status="recommended", location="billing/refunds.py::is_eligible",
    summary="Return PAYMENT_PROFILE_MISSING when no profile exists.",
    code_after="def f(c):\n    if not c.profile:\n        return 'PAYMENT_PROFILE_MISSING'\n",
    regression_test=RegressionTest(name="test_missing_profile", code="def test_missing_profile(): ..."))


def scenario_json(**overrides) -> str:
    base = {"title": "Refund without payment profile",
            "setup": ["Customer exists", "Customer has no saved payment profile"],
            "action": "Attempt a refund for the customer's order.",
            "expected": "The refund is rejected with a clear error.",
            "expected_error_code": "PAYMENT_PROFILE_MISSING"}
    return json.dumps({**base, **overrides})


def run(text, fix=FIX):
    return ScenarioAgent(FakeLLM(text)).run(ISSUE, None, fix)


def test_orchestrator_records_runner_crash():
    from src.api.models import AnalyzeRequest
    from causix_issue_agent import IssueAgent
    from causix_core.reasoning.facts import StubFactsProvider
    from src.reasoning.orchestrator import Orchestrator

    class Boom:
        def run(self, scenario, fix):
            raise RuntimeError("docker down")

    class FixedFix:
        def run(self, issue, rca, lookup):
            return FIX

    llm = FakeLLM(responses=[json.dumps({"summary": "s"}), scenario_json()])
    orch = Orchestrator(IssueAgent(llm), StubFactsProvider(), fix_agent=FixedFix(),
                        scenario_agent=ScenarioAgent(llm), scenario_runner=Boom())
    result = orch.analyze(AnalyzeRequest(issue="x"))
    assert result.scenario.status == "generated" and result.scenario.execution.status == "error"
    assert any("docker down" in n for n in result.notes)
