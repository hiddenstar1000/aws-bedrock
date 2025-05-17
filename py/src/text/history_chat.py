import boto3
import json

client = boto3.client(service_name='bedrock-runtime', region_name="us-west-2")

history = []

def get_history():
    return "\n".join(history)

def get_configuration(prompt: str):
    return json.dumps({
        "inputText": prompt + "\n" + get_history(),
        "textGenerationConfig": {
            "maxTokenCount": 4096,
            "stopSequences": [],
            "temperature": 0,
            "topP": 1
        }
    })

while True:
    user_input = input("User: ")
    history.append("User: " + user_input)
    if user_input.lower() == "exit":
        break
    response = client.invoke_model(
        body=get_configuration(user_input),
        modelId="amazon.titan-text-express-v1",
        accept="application/json",
        contentType="application/json")
    response_body = json.loads(response.get('body').read())
    output_text = response_body.get('results')[0].get('outputText').strip()
    print(output_text)
    history.append(output_text)