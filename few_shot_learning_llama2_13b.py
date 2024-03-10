import boto3
import json


prompt_txt="""
You are a very intelligent bot with exceptional language skills

"""

context = """

A "lemurwhat" is a small, furry animal native to Tanzania. An example of a sentence that uses the word lemurwhat is:
We were traveling in Africa and we saw these very cute lemurwhats
To do a "cuteduddle" means to jump up and down really fast. 
An example of a sentence that uses the word cuteduddle is:

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

