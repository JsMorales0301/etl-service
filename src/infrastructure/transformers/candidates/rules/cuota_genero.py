import pandas as pd
from src.domain.interfaces.rule import Rule
from typing import Any

class CuotaGenero(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        
        df = data
        quota = context.get("gender_quota", 30) if context else 30
        percent_quota = quota / 100

        list_group = ["codigo_corporacion", "codigo_circunscripcion", "nombre_partido"]

        df_filtered = df[df["numero_candidato"] != "999"]

        df_grouped = (
            df_filtered.groupby(list_group)
            .agg(
                candidate_len=("primer_nombre", "count"),
                men_len=("genero_candidato", lambda x: sum(g in ["M", "T", "N"] for g in x)),
                women_len=("genero_candidato", lambda x: sum(g == "F" for g in x)),
            )
            .reset_index()
        )

        df_grouped["percent_men"] = df_grouped["men_len"] / df_grouped["candidate_len"]
        df_grouped["percent_women"] = df_grouped["women_len"] / df_grouped["candidate_len"]

        df_grouped["women_quota_met"] = df_grouped["percent_women"] >= percent_quota
        df_grouped["men_quota_met"] = df_grouped["percent_men"] >= percent_quota

        df_invalid_quota = df_grouped[
            (df_grouped["candidate_len"] > 5)
            & (~df_grouped["women_quota_met"] | ~df_grouped["men_quota_met"])
        ]