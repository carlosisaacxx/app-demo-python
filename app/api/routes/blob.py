from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from pathlib import Path
import pandas as pd

from app.services.blob_service import upload_and_download_files
from app.services.file_service import generate_sample_files

router = APIRouter()

@router.get("/generate-csv-to-json")
async def convert_csv_to_json():
    try:
        csv_path = Path("data/filecreate/people.csv")
        if not csv_path.exists():
            return JSONResponse(
                status_code=404, 
                content={
                    "error": "file people.csv not found",
                    "message": "Please generate sample files first using the endpoint /generate-sample-files"
                }
            )
        
        df = pd.read_csv(csv_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return JSONResponse(
            status_code=500, 
            content={"error": str(e)}
        )
    
@router.post("/upload-local")
async def upload_to_local(file: UploadFile = File(...)):
    save_path = Path("data/filecreate") / file.filename
    contents = await file.read()
    save_path.write_bytes(contents)
    return JSONResponse(
        status_code=200, 
        content={
            "message": f"File {file.filename} uploaded successfully to local storage."
            }
    )

@router.post("/upload-blob")
async def upload_to_blob():
    try:
        upload_and_download_files()
        return JSONResponse(
            status_code=200, 
            content={"message": "Files uploaded successfully to Azure Blob Storage."}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500, 
            content={"error": str(e)}
        )
    
@router.get("/download-blob")
async def download_from_blob():
    try:
        upload_and_download_files()
        return JSONResponse(
            status_code=200, 
            content={"message": "Files downloaded successfully from Azure Blob Storage."}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500, 
            content={"error": str(e)}
        )