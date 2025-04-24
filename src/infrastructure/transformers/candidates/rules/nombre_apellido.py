import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class NombreApellido(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        
        df_name = df[
            (df["primer_nombre"].isna())
            | (df["primer_nombre"] == "")
            | (df["primer_apellido"].isna())
            | (df["primer_apellido"] == "")
        ]   