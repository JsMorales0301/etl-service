import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class TablaParametrica(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data

        df_departments, df_cities = context["candidate_repository"].get_departments_and_cities()

        df_departments["codigo_divipole"] = (
            df_departments["codigo_divipole"].astype(str).apply(lambda x: x.zfill(2))
        )
        df_cities["codigo_divipole"] = (
            df_cities["codigo_divipole"].astype(str).apply(lambda x: x.zfill(3))
        )

        df_result_depto = df["codigo_departamento"].isin(df_departments["codigo_divipole"])
        df_result_cities = df["codigo_municipio"].isin(df_cities["codigo_divipole"])
        