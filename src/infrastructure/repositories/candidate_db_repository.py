from src.domain.interfaces.candidate_repository import CandidateRepository
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

import pandas as pd

class CandidateDBRepository(CandidateRepository):

    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)

    def get_corporations_by_id_election(self, id_electoral_process: str) -> pd.DataFrame:
        
        try:
            with self.engine.connect() as connection:
                query_corp = """
                    SELECT c.orden, c.titulo, c.tipo_corporacion 
                    FROM kits_electorales.corporaciones c
                    WHERE c.id_proceso_electoral = :id_proceso
                    ORDER BY c.orden
                """

                df_corporations = pd.read_sql(query_corp, connection, params={"id_proceso": id_electoral_process})

            return df_corporations
        
        except SQLAlchemyError as e:
            print(f"[ERROR] error al consultar las corporaciones: {str(e)}")