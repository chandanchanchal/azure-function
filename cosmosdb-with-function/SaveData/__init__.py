import azure.functions as func
import json
from shared.cosmos_client import container

def main(req: func.HttpRequest) -> func.HttpResponse:
    data = json.loads(req.get_body())
    container.upsert_item(data)
    return func.HttpResponse("Item saved successfully", status_code=201)
