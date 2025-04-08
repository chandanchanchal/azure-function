from azure.cosmos import CosmosClient, PartitionKey, exceptions

# Cosmos DB config (move to env variables in production)
COSMOS_URI = "https://<your-account>.documents.azure.com:443/"
COSMOS_KEY = "<your-key>"
DATABASE_NAME = "TravelDB"
CONTAINER_NAME = "Bookings"

client = CosmosClient(COSMOS_URI, credential=COSMOS_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)


def create_booking(data):
    try:
        container.create_item(body=data)
        return {"message": "Booking created", "data": data}, 201
    except exceptions.CosmosHttpResponseError as e:
        return {"error": str(e)}, 500


def get_booking(booking_id):
    try:
        response = container.read_item(item=booking_id, partition_key=booking_id)
        return response, 200
    except exceptions.CosmosResourceNotFoundError:
        return {"error": "Booking not found"}, 404


def update_booking(booking_id, updated_data):
    try:
        item = container.read_item(item=booking_id, partition_key=booking_id)
        for key in updated_data:
            item[key] = updated_data[key]
        container.replace_item(item=booking_id, body=item)
        return {"message": "Booking updated", "data": item}, 200
    except exceptions.CosmosResourceNotFoundError:
        return {"error": "Booking not found"}, 404


def delete_booking(booking_id):
    try:
        container.delete_item(item=booking_id, partition_key=booking_id)
        return {"message": "Booking deleted"}, 200
    except exceptions.CosmosResourceNotFoundError:
        return {"error": "Booking not found"}, 404
