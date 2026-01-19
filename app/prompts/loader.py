
import random, pathlib

def load_prompt():
    version = "v2" if random.randint(1,10)==1 else "v1"
    path = pathlib.Path(f"prompts/{version}/system.md")
    return path.read_text(), version
