from fastapi import APIRouter, UploadFile, File
from src.application.use_cases.etl_process import ETLProcess
from src.domain.models.request_data import RequestData
from src.domain.datatypes.candidates import dtype_candidates
from src.infrastructure.api.api_controller import APIController

import os

# Crear instancia del controlador
api_controller = APIController()

# Obtener el router
router = api_controller.router

    