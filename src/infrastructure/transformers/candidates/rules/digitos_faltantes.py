import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class DigitosFaltantes(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        df["department_valid"] = (
            df["codigo_departamento"].astype(str).apply(lambda x: len(x) == 2)
        )

        df["municipe_valid"] = df["codigo_municipio"].astype(str).apply(lambda x: len(x) == 3)
        df["comuna_valid"] = df["codigo_comuna"].astype(str).apply(lambda x: len(x) == 2)

        df[~df["comuna_valid"]]
        