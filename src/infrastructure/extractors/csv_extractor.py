from src.domain.interfaces.extract import Extract
from src.domain.models.options import Options

import pandas as pd

class CsvExtractor(Extract):

    def extract_from_file(self, path: str, options: Options) -> pd.DataFrame:

        config = options.model_dump()

        try:
            return pd.read_csv(
                path,   
                sep=config['sep'],
                low_memory=config['low_memory'],
                encoding=config['encoding'],
                header=config['header'],
                names=config['names'],
                dtype=config['dtype']
            )
        except Exception as e:
            raise ValueError(f"Error al leer el archivo {path}: {str(e)}")
    