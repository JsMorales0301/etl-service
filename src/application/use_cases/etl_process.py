from src.infrastructure.extractors.extractor_factory import ExtractorFactory
from src.infrastructure.transformers.strategy_factory import TransformFactory
from src.domain.models.request_data import RequestData
from src.infrastructure.repositories.candidate_db_repository import CandidateDBRepository

class ETLProcess:

    def __init__(self):
        pass

    def execute(self, data: RequestData):
        extractor = ExtractorFactory()
        transform = TransformFactory()
        file_path = data.file_path
        options = data.options
        type_file = data.type_file
        
        candidate_repo = CandidateDBRepository(connection_string="postgresql://postgres:1234@localhost:5433/kits_electorales")

        context = {
            "gender_quota": data.gender_quota,
            "id_electoral_process": data.id_electoral_process,
            "candidate_repository": candidate_repo
        }

        df = extractor.get_extractor(type_file).extract_from_file(file_path, options)
        transform.get_strategy('candidatos').run(df, context)
        
        
