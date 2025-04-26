import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class EstadoLista(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        
        repo = context.get("candidate_repository")
        id_electoral_process = context.get("id_electoral_process")
        df_corporations = repo.get_corporations_by_id(id_electoral_process)
        
        values_unipersonal = ["RETIRADO", "REVOCADO", ""]
        values_list = ["LISTA RETIRADA", "LISTA REVOCADA", "RETIRADO", ""]

        df_unipersonal = df_corporations[
            df_corporations["tipo_corporacion"] == "1 - Unipersonales"
        ]
        df_list = df_corporations[df_corporations["tipo_corporacion"] == "2 - Listas"]

        df_filter_unipersonal = df[df["codigo_corporacion"].isin(df_unipersonal["orden"])]
        df_filter_list = df[df["codigo_corporacion"].isin(df_list["orden"])]

        df_filter_unipersonal[
            ~df_filter_unipersonal["estado_lista"].fillna("").isin(values_unipersonal)
        ]["estado_lista"]
        df_filter_list[~df_filter_list["estado_lista"].fillna("").isin(values_list)][
            "estado_lista"
        ]