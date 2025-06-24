from azure.storage.blob import BlobServiceClient

AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=your_account_name;AccountKey=your_account_key;EndpointSuffix=core.windows.net"
CONTAINER = "your_container_name"

blob_service = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
blob_client = blob_service.get_blob_client(container=CONTAINER, blob="people.csv")

# Event upload
with open("people.csv", "rb") as data:
    blob_client.upload_blob(data, overwrite=True)
if __name__ == "__main__":
    print("File uploaded successfully to Azure Blob Storage: people.csv")

# Event download
downloaded = blob_client.download_blob().readall()
with open("downloaded_people.csv", "wb") as file:
    file.write(downloaded)
if __name__ == "__main__":
    print("File downloaded successfully from Azure Blob Storage: downloaded_people.csv")
    print("Make sure to check the file in your local directory.")