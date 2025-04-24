from src.domain.interfaces.rule import Rule
from typing import Any
import time
from .rules.documento_repetido import DocumentoRepetido
from .rules.doble_militancia import DobleMilitancia
from .rules.documento_sin_letras import DocumentoSinLetras
from .rules.cuota_genero import CuotaGenero
from .rules.nombre_apellido import NombreApellido
from .rules.generos_permitidos import GenerosPermitidos
from .rules.nombres_apellidos_mayuscula import NombresApellidosMayusculas

class CandidatesStrategy:

    rules: list[Rule]

    def __init__(self):
        self.rules = [
            DocumentoRepetido(),
            DobleMilitancia(),
            DocumentoSinLetras(),
            CuotaGenero(),
            NombreApellido(),
            GenerosPermitidos(),
            NombresApellidosMayusculas()
        ]

    def run(self, df, context: dict[str, Any] = None):
        start = time.time()
        for rule in self.rules:
            rule.apply(df, context)
        end = time.time()
        print(f"Tiempo de ejecución: {end - start:.6f} segundos")
        return df