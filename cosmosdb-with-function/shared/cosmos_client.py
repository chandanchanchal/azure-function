import os
from azure.cosmos import CosmosClient

url = os.environ["COSMOS_URI"]
key = os.environ["COSMOS_KEY"]
database_name = os.environ["COSMOS_DB"]
container_name = os.environ["COSMOS_CONTAINER"]

client = CosmosClient(url, credential=key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)
