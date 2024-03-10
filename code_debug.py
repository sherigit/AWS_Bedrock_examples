import boto3
import json


prompt_txt="""
Find the issue in this code below. Explain your reason

import torch
torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
def run_som_func(a, b):
    c = c*2
    c=a+b
    print(c)
    return c ^ 2
I get an error saying variable referred before

"""

bedrock=boto3.client(service_name="bedrock-runtime")
prompt_template = "[INST]"+ prompt_txt +"[/INST]"

payload={
    "prompt":prompt_template,
    "max_gen_len":512,
    "temperature":0.5,
    "top_p":0.9
}
body=json.dumps(payload)
model_id="meta.llama2-13b-chat-v1"

response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())
repsonse_text=response_body['generation']
print(repsonse_text)
