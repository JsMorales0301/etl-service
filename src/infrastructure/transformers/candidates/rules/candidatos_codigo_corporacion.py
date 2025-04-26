import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class CandidatosCodigoCorporacion(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        df_filtered = df[df["numero_candidato"] != 999]

        list_groupby = [
            "numero_identificacion",
            "codigo_corporacion",
            "codigo_departamento",
            "codigo_comuna",
            "codigo_municipio",
            "codigo_partido",
            "numero_candidato",
        ]

        group_sizes = df_filtered.groupby(list_groupby)["numero_identificacion"].transform(
            "size"
        )

        duplicated = df_filtered[group_sizes > 1]

        result = duplicated[["numero_identificacion", "primer_nombre"]]
        