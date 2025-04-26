import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class EstructuraNumeroCandidato(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        df["numero_candidato_empty"] = df["numero_candidato"].notna()
        df["numero_candidato_range"] = (df["numero_candidato"] >= 1) & (df["numero_candidato"] <= 502)

        df_filtered_candidate = df[df["numero_candidato"] != 999]
