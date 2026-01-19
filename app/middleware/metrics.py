
from prometheus_client import Counter
tokens_counter = Counter("llm_tokens_total","Total LLM tokens",["prompt_version"])

def record_metrics(tokens, version):
    tokens_counter.labels(prompt_version=version).inc(tokens)
