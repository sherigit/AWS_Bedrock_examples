import boto3
import json

meetings_txt="""  User: Generate synthetic data for daily product sales in various categories - include row number, product name, category, date of sale and price. 

        Produce output in JSON format. Count records and ensure there are no more than 5.
  
  Bot:
            
"""

bedrock=boto3.client(service_name="bedrock-runtime")
prompt_template = meetings_txt

txt_config_template = {
    "maxTokenCount":1024,
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
