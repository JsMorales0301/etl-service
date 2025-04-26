from src.domain.interfaces.candidate_repository import CandidateRepository
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

import pandas as pd

class CandidateDBRepository(CandidateRepository):

    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)

    def get_corporations_by_id_election(self, id_electoral_process: str) -> pd.DataFrame:
        
        try:
            with self.engine.connect() as connection:
                query_corp = text("""
                    SELECT c.orden, c.titulo, c.tipo_corporacion 
                    FROM kits_electorales.corporaciones c
                    WHERE c.id_proceso_electoral = :id_proceso
                    ORDER BY c.orden
                """)

                df_corporations = pd.read_sql(query_corp, connection, params={"id_proceso": id_electoral_process})

            return df_corporations
        
        except SQLAlchemyError as e:
            print(f"[ERROR] error al consultar las corporaciones: {str(e)}")

    def get_departments_and_cities(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        try:
            with self.engine.connect() as connection:
                query_departments = """
                    SELECT * FROM kits_electorales.departamentos
                """
                query_cities = """
                    SELECT * FROM kits_electorales.ciudades
                """

                df_departments = pd.read_sql(query_departments, connection)
                df_cities = pd.read_sql(query_cities, connection)

                return df_departments, df_cities

        except SQLAlchemyError as e:
            print(f"[ERROR] error al consultar departamentos y ciudades: {str(e)}")
            return pd.DataFrame(), pd.DataFrame()  # Retorna ambos vacíos si falla
        
    def get_corporations_by_id(self, id_proceso: str) -> pd.DataFrame:
        try:
            with self.engine.connect() as connection:
                query_corp = text("""
                    SELECT c.orden, c.titulo, c.tipo_corporacion 
                    FROM kits_electorales.corporaciones c
                    WHERE c.id_proceso_electoral = :id_proceso
                    ORDER BY c.orden
                """)
                df_corporations = pd.read_sql(query_corp, connection, params={"id_proceso": id_proceso})

                # Procesamiento de tipos
                df_corporations["orden"] = pd.to_numeric(df_corporations["orden"], errors="coerce")
                df_corporations["tipo_corporacion"] = df_corporations["tipo_corporacion"].astype(str)

                return df_corporations

        except SQLAlchemyError as e:
            print(f"[ERROR] error al consultar corporaciones: {str(e)}")
            return pd.DataFrame()