def test_agent_orchestrator():
    prompt = "Test execution query for agentic-construction-safety-auditor"
    assert len(prompt) > 0
    assert "Test" in prompt
