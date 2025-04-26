from src.domain.interfaces.candidate_repository import CandidateRepository
from src.infrastructure.config.database_config import DatabaseConfig
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

import pandas as pd

class CandidateDBRepository(CandidateRepository):

    def __init__(self, config: DatabaseConfig):
        self.config = config
        self.engine = create_engine(config.connection_string)

    def get_corporations_by_id_election(self, id_electoral_process: str) -> pd.DataFrame:
        
        try:
            with self.engine.connect() as connection:
                query_corp = text(f"""
                    SELECT c.orden, c.titulo, c.tipo_corporacion 
                    FROM {self.config.schema}.corporaciones c
                    WHERE c.id_proceso_electoral = :id_proceso
                    ORDER BY c.orden
                """)

                df_corporations = pd.read_sql(query_corp, connection, params={"id_proceso": id_electoral_process})

            return df_corporations
        
        except SQLAlchemyError as e:
            print(f"[ERROR] error al consultar las corporaciones: {str(e)}")
            return pd.DataFrame()

    def get_departments_and_cities(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        try:
            with self.engine.connect() as connection:
                query_departments = f"""
                    SELECT * FROM {self.config.schema}.departamentos
                """
                query_cities = f"""
                    SELECT * FROM {self.config.schema}.ciudades
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
                query_corp = text(f"""
                    SELECT c.orden, c.titulo, c.tipo_corporacion 
                    FROM {self.config.schema}.corporaciones c
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