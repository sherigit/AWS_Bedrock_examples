import boto3
import json


prompt_txt="""
Turn the following product feature into a list of benefits. Then, group this list of benefits into three types of benefits: Functional Benefits, Emotional Benefits, and Social Benefits.

Product Feature:Our app automatically transcribes your meetings. It uses state-of-the-art speech-to-text technology that works even in noisy backgrounds. 
  Once the transcription is done, our app creates its summary and automatically emails it to the meeting attendees.
"""


bedrock=boto3.client(service_name="bedrock-runtime")
prompt_template = prompt_txt 

payload={
    "prompt":prompt_template,
    "max_tokens":200,
    "temperature":0.5,
    "p":0.75, 
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
response_text=response_body['generations'][0]['text']

#print(response_body)
print("=========================================")
print(response_text)
print("=========================================")
