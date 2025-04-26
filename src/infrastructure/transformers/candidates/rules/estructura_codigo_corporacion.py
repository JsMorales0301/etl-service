import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class EstructuraCodigoCorporacion(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        print("Hola")
        df["range_valid"] = (df["codigo_corporacion"] >= 1) & (df["codigo_corporacion"] <= 9)
        df["code_corporation_empty"] = df["codigo_corporacion"].notna()
        df[~df["code_corporation_empty"]]
        