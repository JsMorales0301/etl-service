import pandas as pd
import numpy as np
from src.domain.interfaces.rule import Rule
from typing import Any

class NombresApellidosMayusculas(Rule[pd.DataFrame]):
    name = "candidatos_validar_documento"

    def apply(self, data: pd.DataFrame, context: dict[str, Any] | None = None):
        df = data
        
        df["primer_nombre"] = df["primer_nombre"].fillna("").astype(str)
        df["primer_apellido"] = df["primer_apellido"].fillna("").astype(str)

        nombres_array = df["primer_nombre"].to_numpy(dtype="str")
        apellidos_array = df["primer_apellido"].to_numpy(dtype="str")

        nombres_mayusculas = np.char.isupper(nombres_array)
        apellidos_mayusculas = np.char.isupper(apellidos_array)

        df["informacion_valida"] = nombres_mayusculas & apellidos_mayusculas

        filas_invalidas = df[~df["informacion_valida"]]