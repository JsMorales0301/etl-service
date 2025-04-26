import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class EstructuraNumeroIdentificacion(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        
        df["num_ident_empty"] = df["numero_identificacion"].isna()
        df["num_ident_range"] = (df["numero_identificacion"] >= "1") & (
            df["numero_identificacion"] <= "20000000000"
        )
        