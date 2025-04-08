import logging
import azure.functions as func
import json
from cosmos_helper import create_booking, get_booking, update_booking, delete_booking

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing a request.")
    method = req.method
    try:
        if method == "POST":
            data = req.get_json()
            response, code = create_booking(data)
        elif method == "GET":
            booking_id = req.params.get("id")
            if not booking_id:
                return func.HttpResponse("Missing id param", status_code=400)
            response, code = get_booking(booking_id)
        elif method == "PUT":
            booking_id = req.params.get("id")
            if not booking_id:
                return func.HttpResponse("Missing id param", status_code=400)
            data = req.get_json()
            response, code = update_booking(booking_id, data)
        elif method == "DELETE":
            booking_id = req.params.get("id")
            response, code = delete_booking(booking_id)
        else:
            return func.HttpResponse("Method not allowed", status_code=405)

        return func.HttpResponse(json.dumps(response), status_code=code, mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(json.dumps({"error": str(e)}), status_code=500)
