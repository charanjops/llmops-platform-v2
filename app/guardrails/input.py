
FORBIDDEN_PATTERNS=["ignore previous","system prompt","jailbreak"]
MAX_INPUT_LENGTH=2000

def validate_input(text):
    if len(text)>MAX_INPUT_LENGTH:
        raise ValueError("Input too long")
    for p in FORBIDDEN_PATTERNS:
        if p in text.lower():
            raise ValueError("Prompt injection detected")
