from src.domain.models.options import Options
from pydantic import BaseModel

class RequestData(BaseModel):
    file_path: str
    options: Options
    type_file: str
    gender_quota: int
    id_electoral_process: str
