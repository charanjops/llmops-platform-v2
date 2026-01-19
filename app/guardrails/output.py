
UNSAFE=["illegal","violence","hate"]

def validate_output(text):
    for u in UNSAFE:
        if u in text.lower():
            raise ValueError("Unsafe output")
    if not text.strip():
        raise ValueError("Empty output")
    return text
