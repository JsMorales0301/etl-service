import pandas as pd
from typing import Any
from src.domain.interfaces.rule import Rule

class GenerosPermitidos(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        
        genders = {"F", "M", "T", "N"}
        df["gender_valid"] = df["genero_candidato"].isin(genders) 