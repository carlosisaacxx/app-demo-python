from pathlib import Path
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError
from app.config import AZURE_STORAGE_CONNECTION_STRING, BLOB_CONTAINER, BLOB_PREFIX

blob_service = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

BASE_DIR_CREATE = Path('data/filecreate')
BASE_DIR_DOWNLOAD = Path('data/filedownloaded')
BASE_DIR_CREATE.mkdir(parents=True, exist_ok=True)
BASE_DIR_DOWNLOAD.mkdir(parents=True, exist_ok=True)

def upload_and_download_files():
    container_client = blob_service.get_container_client(BLOB_CONTAINER)
    try:
        container_client.create_container()
        print(f"[OK] Contenedor '{BLOB_CONTAINER}' creado")
    except ResourceExistsError:
        print(f"[INFO] Contenedor '{BLOB_CONTAINER}' ya existe")

    for file_path in BASE_DIR_CREATE.iterdir():
        if file_path.is_file():
            blob_name = f"{BLOB_PREFIX}/{file_path.name}" if BLOB_PREFIX else file_path.name
            blob_client = container_client.get_blob_client(blob_name)

            with file_path.open('rb') as data:
                blob_client.upload_blob(data, overwrite=True)
            print(f"[OK] 📤 Subido: {blob_name}")

            output_path = BASE_DIR_DOWNLOAD / f"downloaded_{file_path.name}"
            output_path.write_bytes(blob_client.download_blob().readall())
            print(f"[OK] 📥 Descargado: {output_path}")