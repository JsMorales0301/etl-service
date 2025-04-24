import pandas as pd
from src.domain.interfaces.rule import Rule
from typing import Any

class DocumentoRepetido(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        
        df_filtered = df[df["numero_candidato"] != 999]

        df_filtered = df_filtered[
            df_filtered.duplicated(["numero_identificacion", "nombre_partido"], keep=False)
        ]