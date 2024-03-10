import boto3
import json

meetings_txt=""" 
"User: Product: Sunglasses.
Keywords: polarized, designer, comfortable, UV protection, aviators.

Create a table that contains five variations of a detailed product description for the product listed above, each variation of the product description must use all the keywords listed.

Bot: ,

"""

bedrock=boto3.client(service_name="bedrock-runtime")
prompt_template = meetings_txt

txt_config_template = {
    "maxTokenCount":4096,
    "stopSequences":["User:"],
    "temperature":0, 
    "topP":1
}

payload={
    "inputText":prompt_template,
    "textGenerationConfig" : txt_config_template    
}

body=json.dumps(payload)
model_id="amazon.titan-text-express-v1"

response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())
#repsonse_text=response_body['generation']
#print(response_body)

response_text=response_body['results'][0]['outputText']

print(response_text) 