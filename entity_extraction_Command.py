import boto3
import json


prompt_txt="""
Extract the band name from the contract:
"""
context = """
This Music Recording Agreement ("Agreement") is made effective as of the 13 day of December, 2021 by and between Good Kid, 
a Toronto-based musical group (“Artist”) and Universal Music Group, 
a record label with license number 545345 (“Recording Label"). 
Artist and Recording Label may each be referred to in this Agreement individually as a "Party" and collectively as the "Parties." 
Work under this Agreement shall begin on March 15, 2022.",

"""

bedrock=boto3.client(service_name="bedrock-runtime")
prompt_template = prompt_txt + context

payload={
    "prompt":prompt_template,
    "max_tokens":200,
    "temperature":0.9,
    "p":1,
    "k":0
}

body=json.dumps(payload)
model_id="cohere.command-text-v14"

response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())
#response_text=response_body['generation']
print(response_body['generations'][0]['text'])
