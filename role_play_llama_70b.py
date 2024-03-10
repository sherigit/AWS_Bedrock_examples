import boto3
import json


prompt_txt="""
You are a Data scientist trying to explain to a 5 year old
"""

context = """ 
Can you explain what is a transformer in a machine learning context ?
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
repsonse_text=response_body['generation']
print(repsonse_text) 





