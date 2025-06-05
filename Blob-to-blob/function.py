import logging
import os
import io
from PIL import Image
import azure.functions as func
from azure.storage.blob import BlobServiceClient

# Set destination storage connection string in Application Settings
DEST_CONN_STR = os.getenv("AzureWebJobsDestinationStorage")

def resize_image(image_bytes):
    with Image.open(io.BytesIO(image_bytes)) as img:
        img = img.convert("RGB")
        img.thumbnail((300, 300))  # Resize to 300x300 max
        output = io.BytesIO()
        img.save(output, format="JPEG")
        output.seek(0)
        return output.read()

def main(blob: func.InputStream):
    name = blob.name.split("/")[-1]
    if not (name.endswith(".png") or name.endswith(".jpeg") or name.endswith(".jpg")):
        logging.info(f"Skipped file: {name}")
        return

    logging.info(f"Processing image: {name}")

    resized_data = resize_image(blob.read())

    # Upload to destination storage
    blob_service_client = BlobServiceClient.from_connection_string(DEST_CONN_STR)
    container_client = blob_service_client.get_container_client("processed-image")
    container_client.upload_blob(name, resized_data, overwrite=True)

    logging.info(f"Uploaded resized image: {name}")
