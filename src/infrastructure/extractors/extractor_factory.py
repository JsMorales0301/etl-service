from src.infrastructure.extractors.csv_extractor import CsvExtractor

class ExtractorFactory:

    def __init__(self):
        self.extractors = {
            'csv': CsvExtractor,
            'txt': CsvExtractor
        }
    
    def get_extractor(self, type: str):
        extractor = self.extractors.get(type)
        
        if extractor:
            return extractor()
        else:
            raise ValueError(f"Extensión de archivo no valida: {type}")
    
    