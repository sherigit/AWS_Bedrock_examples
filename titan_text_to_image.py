import boto3
import json
import base64
import os


prompt_txt = """ 
             blue backpack on a table
"""
txt_img_param = {"text":prompt_txt}

bedrock = boto3.client(service_name = "bedrock-runtime")

img_config_template = {
    "cfgScale":8,
    "seed":0,
    "quality":"standard",
    "width":512,
    "height":512,
    "numberOfImages":1
}

payload = {
    "textToImageParams":txt_img_param ,
     "taskType":"TEXT_IMAGE",
    "imageGenerationConfig":img_config_template
}

body = json.dumps(payload)

model_id = "amazon.titan-image-generator-v1"

response = bedrock.invoke_model( 
    body = body,
    modelId = model_id,
    accept="application/json",
    contentType = "application/json",
)

response_body = json.loads(response.get("body").read())

print("===================================================")

print(response_body) 

print("===================================================")


#artifact = response_body.get("artifacts")
#image_encoded = response_body.get("base64").encode("utf-8")
#image_bytes = base64.b64decode(image_encoded)

# Save image to a file in the output directory.
output_dir = "output1"
os.makedirs(output_dir, exist_ok=True)
file_name = f"{output_dir}/generated-img.png"
with open(file_name, "wb") as f:
    f.write(response_body[0])

