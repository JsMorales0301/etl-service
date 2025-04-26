import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class EstructuraCodigoCircunscripcion(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        df["range_valid_circ"] = (df["codigo_circunscripcion"] >= 1) & (
            df["codigo_circunscripcion"] <= 9
        )
        df["code_circ_empty"] = df["codigo_circunscripcion"].notna()

        df[~df["code_circ_empty"]]