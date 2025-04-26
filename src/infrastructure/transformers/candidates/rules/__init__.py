from .documento_repetido import DocumentoRepetido
from .doble_militancia import DobleMilitancia
from .documento_sin_letras import DocumentoSinLetras
from .cuota_genero import CuotaGenero
from .nombre_apellido import NombreApellido
from .generos_permitidos import GenerosPermitidos
from .nombres_apellidos_mayuscula import NombresApellidosMayusculas
from .corporacion_unipersonal import CorporacionUnipersonal
from .eleccion_departamental import EleccionDepartamental
from .candidatos_codigo_corporacion import CandidatosCodigoCorporacion
from .digitos_faltantes import DigitosFaltantes
from .TablaParametrica import TablaParametrica
from .estructura_orden_candidato import EstructuraOrdenCandidato
from .estructura_codigo_corporacion import EstructuraCodigoCorporacion
from .estructura_codigo_circunscripcion import EstructuraCodigoCircunscripcion
from .estructura_opcion_voto import EstructuraOpcionVoto
from .estructura_numero_candidato import EstructuraNumeroCandidato
from .retirados_apellido_a import RetiradosApellido
from .estado_lista import EstadoLista
from .letra_partido import LetraPartido
from .estructura_numero_identificacion import EstructuraNumeroIdentificacion
from .estructura_genero_candidato import EstructuraGeneroCandidato

# Agrupación de reglas por categoría
documento_rules = [
    DocumentoRepetido,
    DocumentoSinLetras,
    EstructuraNumeroIdentificacion
]

militancia_rules = [
    DobleMilitancia
]

genero_rules = [
    CuotaGenero,
    GenerosPermitidos,
    EstructuraGeneroCandidato
]

nombre_rules = [
    NombreApellido,
    NombresApellidosMayusculas
]

estructura_rules = [
    EstructuraOrdenCandidato,
    EstructuraCodigoCorporacion,
    EstructuraCodigoCircunscripcion,
    EstructuraOpcionVoto,
    EstructuraNumeroCandidato
]

corporacion_rules = [
    CorporacionUnipersonal,
    CandidatosCodigoCorporacion
]

otros_rules = [
    EleccionDepartamental,
    DigitosFaltantes,
    TablaParametrica,
    RetiradosApellido,
    EstadoLista,
    LetraPartido
]

# Lista completa de reglas
all_rules = (
    documento_rules +
    militancia_rules +
    genero_rules +
    nombre_rules +
    estructura_rules +
    corporacion_rules +
    otros_rules
) 