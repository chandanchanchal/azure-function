import azure.functions as func
from shared.cosmos_client import container

def main(req: func.HttpRequest) -> func.HttpResponse:
    item_id = req.params.get("id")
    if not item_id:
        return func.HttpResponse("ID is required", status_code=400)

    try:
        item = container.read_item(item=item_id, partition_key=item_id)
        return func.HttpResponse(str(item), mimetype="application/json")
    except Exception as e:
        return func.HttpResponse("Item not found", status_code=404)
