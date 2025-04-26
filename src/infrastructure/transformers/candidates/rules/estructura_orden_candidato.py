import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class EstructuraOrdenCandidato(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data

        df["orden_candidato"].isna().all()
        df["is_consecutive"] = df["orden_candidato"].diff().fillna(1) == 1
        all_consecutive = df["is_consecutive"].all()
        df[~df["is_consecutive"]]
        