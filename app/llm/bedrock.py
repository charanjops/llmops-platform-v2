
import boto3
import json
client = boto3.client("bedrock-runtime", region_name="us-east-1")

def call_bedrock(system_prompt, user_prompt):
    prompt = f"\n\nHuman: {system_prompt}\n{user_prompt}\n\nAssistant:"
    response = client.invoke_model(
        modelId="anthropic.claude-v2",
        body=json.dumps({"prompt": prompt,"max_tokens_to_sample": 300}),
        contentType="application/json"
    )
    result = json.loads(response["body"].read())
    text = result["completion"]
    tokens = len(text.split())
    return text, tokens
