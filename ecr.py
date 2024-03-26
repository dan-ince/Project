import boto3

ecr_client = boto3.client('ecr')

repository_name = "system-monitoring-app"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_url = response['repository']['repositoryUrl']
print(repository_url)