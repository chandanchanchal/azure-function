import azure.functions as func
from shared.cosmos_client import container

def main(req: func.HttpRequest) -> func.HttpResponse:
    item_id = req.params.get("id")
    if not item_id:
        return func.HttpResponse("ID is required", status_code=400)

    try:
        container.delete_item(item=item_id, partition_key=item_id)
        return func.HttpResponse("Item deleted", status_code=200)
    except Exception as e:
        return func.HttpResponse("Item not found", status_code=404)
