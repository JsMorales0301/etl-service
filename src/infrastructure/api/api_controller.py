from fastapi import APIRouter, UploadFile, File
from src.application.use_cases.etl_process import ETLProcess
from src.domain.models.request_data import RequestData
from src.domain.datatypes.candidates import dtype_candidates
from src.infrastructure.config.database_config import DatabaseConfig
from src.infrastructure.config.file_config import FileConfig
import os
from typing import Dict, Any

class APIController:
    def __init__(self, 
                 file_config: FileConfig = None,
                 db_config: DatabaseConfig = None):
        self.file_config = file_config or FileConfig()
        self.db_config = db_config or DatabaseConfig.from_env()
        self.router = APIRouter()
        self._setup_routes()

    def _setup_routes(self) -> None:
        self.router.get("/test")(self.test)
        self.router.post("/upload/")(self.upload_file)
        self.router.post("/execute/")(self.execute_etl)

    async def test(self) -> Dict[str, str]:
        return {"message": "ETL RUNNING"}

    async def upload_file(self, file: UploadFile = File(...)) -> Dict[str, str]:
        new_filename = self.file_config.generate_filename(file.filename)
        
        file_location = os.path.join(self.file_config.get_temp_path(), new_filename)
        with open(file_location, "wb") as buffer:
            buffer.write(await file.read())
        
        return {
            "original_filename": file.filename,
            "new_filename": new_filename,
            "location": file_location
        }

    def execute_etl(self, data: RequestData) -> Any:
        names = dtype_candidates.keys()
        data.options.names = list(names)
        data.options.dtype = dtype_candidates
        
        etl = ETLProcess(db_config=self.db_config)
        return etl.execute(data) 