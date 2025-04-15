import boto3

bedrock = boto3.client(service_name='bedrock', region_name='us-west-2')

models = bedrock.list_foundation_models()

print(models)