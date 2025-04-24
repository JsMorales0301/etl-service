from fastapi import APIRouter, UploadFile, File
from src.application.use_cases.etl_process import ETLProcess
from src.domain.models.request_data import RequestData
from src.domain.datatypes.candidates import dtype_candidates

import os

router = APIRouter()

UPLOAD_FOLDER = "temp"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.get("/test")
async def test():
    return {"message": "ETL RUNNING"}

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())
    
    return {"filename": file.filename, "location": file_location}

@router.post('/execute/')
def execute_etl(data: RequestData):
    
    names = dtype_candidates.keys()
    data.options.names = list(names)
    data.options.dtype = dtype_candidates
    
    etl = ETLProcess()
    return etl.execute(data)
    