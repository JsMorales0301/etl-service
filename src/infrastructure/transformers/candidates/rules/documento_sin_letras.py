import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class DocumentoSinLetras(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        
        df_invalid = df[df["numero_identificacion"].str.contains(r"[a-zA-Z]", na=False)]
        df_invalid[["numero_identificacion", "primer_nombre"]]