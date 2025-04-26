import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class LetraPartido(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        diccionario = {
            str(i): letra.upper()
            for i, letra in enumerate("abcdefghijklmnñopqrstuvwxyz", start=1)
        }

        list_group = [
            "codigo_corporacion",
            "codigo_circunscripcion",
            "codigo_departamento",
            "codigo_municipio",
            "codigo_comuna",
        ]

        df["letra_partido"] = df["numero_sorteo"].astype(str).map(diccionario)

        df_result = df[list_group + ["numero_sorteo", "letra_partido"]].copy()
        