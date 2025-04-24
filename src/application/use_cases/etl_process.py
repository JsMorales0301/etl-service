from src.infrastructure.extractors.extractor_factory import ExtractorFactory
from src.infrastructure.transformers.strategy_factory import TransformFactory
from src.domain.models.request_data import RequestData

class ETLProcess:

    def __init__(self):
        pass

    def execute(self, data: RequestData):
        extractor = ExtractorFactory()
        transform = TransformFactory()
        file_path = data.file_path
        options = data.options
        type_file = data.type_file
        
        df = extractor.get_extractor(type_file).extract_from_file(file_path, options)
        transform.get_strategy('candidatos').run(df, context={
            "gender_quota": data.gender_quota,
            "id_electoral_process": data.id_electoral_process
        })
        
        
