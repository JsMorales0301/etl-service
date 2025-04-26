import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class EstructuraOpcionVoto(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        df["opc_vote_len"] = df["opcion_voto"].astype(str).str.len() == 1
        df["opc_vote_range"] = (df["opcion_voto"] >= 1) & (df["opcion_voto"] <= 2)