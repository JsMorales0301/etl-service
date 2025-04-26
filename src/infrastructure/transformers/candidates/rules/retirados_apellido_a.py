import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class RetiradosApellido(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        df_filter_candidate = df[df["numero_candidato"] == 999]
        is_all_a = df_filter_candidate["primer_apellido"] == "(A)"
        df_filter_candidate[~is_all_a]["primer_apellido"]
        