from app.services.blob_service import upload_and_download_files
from app.services.file_service import generate_sample_files

def main():
    print("🔧 Utilidades disponibles:")
    print("1. Generar archivos de ejemplo")
    print("2. Subir y descargar archivos desde Azure Blob Storage")
    choice = input("Selecciona una opción (1 o 2): ")

    if choice == "1":
        generate_sample_files()
    elif choice == "2":
        upload_and_download_files()
    else:
        print("❌ Opción inválida.")

if __name__ == '__main__':
    main()