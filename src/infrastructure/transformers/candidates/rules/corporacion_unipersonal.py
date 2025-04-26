import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class CorporacionUnipersonal(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        repo = context.get("candidate_repository")
        id_electoral_process = context.get("id_electoral_process")
        df_corporations = repo.get_corporations_by_id_election(id_electoral_process)

        df_corporation_unipersonal = df_corporations[
            df_corporations["tipo_corporacion"] == "1 - Unipersonales"
        ]
        df_corporation_unipersonal.loc[:, "orden"] = df_corporation_unipersonal["orden"].astype(
            int
        )
        df_filtered = df[df["codigo_corporacion"].isin(df_corporation_unipersonal["orden"])]
        is_valid = df_filtered["opcion_voto"] == 1
        df_invalid = df_filtered[~is_valid]
        