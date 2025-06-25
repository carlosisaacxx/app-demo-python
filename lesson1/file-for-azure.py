# This script uploads all files in lesson1/filecreate to Azure Blob Storage
# and downloads them to lesson1/filedownloaded for verification.

import json
from pathlib import Path
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError, AzureError

# ==================== Cargar configuración ====================
try:
    print("[DEBUG] 📂 Cargando configuración...")
    with open('enviroment/enviroment-dev.json') as f:
        config = json.load(f)
    print("[OK] Configuración cargada correctamente ✅")
except Exception as e:
    print(f"[ERROR] No se pudo leer el archivo enviroment-dev.json: {e}")
    raise

# ==================== Datos de Azure Storage ====================
az_storage_connection_string = config['AZURE_STORAGE_CONNECTION_STRING']
container_info = config['CONTAINERS']['json']
container_name = container_info['name']
blob_prefix = container_info.get('blobPrefix', '')

# ==================== Inicialización ====================
print("[DEBUG] 🔄 Inicializando BlobServiceClient...")
blob_service = BlobServiceClient.from_connection_string(az_storage_connection_string)
container_client = blob_service.get_container_client(container_name)

# ==================== Crear contenedor si no existe ====================
try:
    print(f"[DEBUG] 📂 Creando contenedor '{container_name}' si no existe...")
    container_client.create_container()
    print(f"[OK] Contenedor '{container_name}' creado ✅")
except ResourceExistsError:
    print(f"[INFO] El contenedor '{container_name}' ya existe.")
except AzureError as e:
    print(f"[ERROR] Error creando contenedor: {e}")

# ==================== Directorios locales ====================
base_dir = Path('lesson1')
create_dir = base_dir / 'filecreate'
download_dir = base_dir / 'filedownloaded'
download_dir.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    try:
        # ==================== Procesar cada archivo ====================
        for file_to_upload in create_dir.iterdir():
            if file_to_upload.is_file():
                blob_name = f"{blob_prefix}/{file_to_upload.name}"
                blob_client = blob_service.get_blob_client(container=container_name, blob=blob_name)

                # Subir el blob
                print(f"[DEBUG] 📤 Subiendo '{file_to_upload}' como '{blob_name}'...")
                with file_to_upload.open('rb') as data:
                    blob_client.upload_blob(data, overwrite=True)
                print(f"[OK] 🎉 Archivo subido: {blob_name}")

                # Descargar el blob a filedownloaded
                output_path = download_dir / f"downloaded_{file_to_upload.name}"
                print(f"[DEBUG] 📥 Descargando '{blob_name}' a '{output_path}'...")
                output_path.write_bytes(blob_client.download_blob().readall())
                print(f"[OK] ✅ Archivo descargado correctamente: {output_path}")

        print("[OK] 🎯 Todos los archivos han sido procesados correctamente.")

    except AzureError as e:
        print(f"[ERROR] Ocurrió un error en Azure: {e}")
    except Exception as e:
        print(f"[ERROR] Error inesperado: {e}")