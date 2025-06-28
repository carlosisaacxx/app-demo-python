from dotenv import load_dotenv
import os

load_dotenv()

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
BLOB_CONTAINER = os.getenv("BLOB_CONTAINER")
BLOB_PREFIX = os.getenv("BLOB_PREFIX", "")