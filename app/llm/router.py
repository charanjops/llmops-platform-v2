
from app.llm.openrouter import call_openrouter
from app.guardrails.input import validate_input
from app.guardrails.output import validate_output
from app.guardrails.cost import check_cost
from app.middleware.metrics import record_metrics
from app.prompts.loader import load_prompt

def handle_request(question):
    validate_input(question)
    system_prompt, version = load_prompt()
    raw, tokens = call_openrouter(system_prompt, question)
    check_cost(tokens)
    safe = validate_output(raw)
    record_metrics(tokens, version)
    return {"answer": safe, "prompt_version": version}
