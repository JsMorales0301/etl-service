import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class EleccionDepartamental(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        # Filtrar circunscripciones departamentales
        df_depto = df[df["nombre_circunscripcion"] == "DEPARTAMENTAL"]

        # Validar códigos
        is_valid_depto = df_depto["codigo_departamento"] != 0
        is_valid_mun_com = (df_depto[["codigo_municipio", "codigo_comuna"]] == 0).all(axis=1)

        df_invalid = df_depto[~is_valid_depto | ~is_valid_mun_com]
        df_invalid = df_invalid.reset_index()
        df_invalid = df_invalid.sort_values("index")
        