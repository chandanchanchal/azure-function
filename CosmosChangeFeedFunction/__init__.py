import logging
import azure.functions as func

def main(documents: func.DocumentList) -> None:
    if documents:
        logging.info(f"Documents modified: {len(documents)}")
        for doc in documents:
            logging.info(f"Document content: {doc.to_json()}")
