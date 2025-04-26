import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class EstructuraGeneroCandidato(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        df["gender_len"] = df["genero_candidato"].str.len() == 1
        df["gender_empty"] = df["genero_candidato"].isna()
        