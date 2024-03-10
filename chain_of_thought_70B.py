import boto3
import json


prompt_txt="""
You are a very intelligent bot with exceptional critical thinking
"""
context = """
    I went to the market and bought 10 apples. 
    I gave 2 apples to your friend and 2 to the helper. 
    I then went and bought 5 more apples and ate 1. 
    How many apples did I remain with?

    Let's think step by step."
"""

bedrock=boto3.client(service_name="bedrock-runtime")
prompt_template = "[INST]"+ prompt_txt +"[/INST]" + context

payload={
    "prompt":prompt_template,
    "max_gen_len":512,
    "temperature":0.5,
    "top_p":0.9
}
body=json.dumps(payload)
model_id="meta.llama2-70b-chat-v1"

response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())
response_text=response_body['generation']
print(response_text)
