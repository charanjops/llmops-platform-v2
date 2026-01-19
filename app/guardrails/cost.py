
MAX_TOKENS=2000
def check_cost(tokens):
    if tokens>MAX_TOKENS:
        raise ValueError("Token budget exceeded")
