# import time
from openai import OpenAI
import os

# Load .env only for local development
if os.getenv("ENV", "local") == "local":
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

# Initialize client for OpenRouter
client = OpenAI(
  base_url=os.getenv("OPEN_ROUTER_BASE_URL"),
  api_key=os.getenv("OPEN_ROUTER_API_KEY"),
)

def call_openrouter(system_prompt, user_prompt):
    # start = time.time()
    
    # OpenRouter uses the standard Chat Completions API
    # You can change "anthropic/claude-2" to any model listed on openrouter.ai
    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"), 
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=300
    )
    # Extracting the response text
    text = response.choices[0].message.content
       
    # OpenRouter/OpenAI provides actual token counts in the metadata
    tokens = response.usage.completion_tokens
    
    # duration = time.time() - start
    return text, tokens