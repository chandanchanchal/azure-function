import azure.functions as func
from shared.cosmos_client import container

def main(req: func.HttpRequest) -> func.HttpResponse:
    items = list(container.read_all_items())
    return func.HttpResponse(str(items), mimetype="application/json")
