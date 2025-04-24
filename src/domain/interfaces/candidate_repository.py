from abc import ABC, abstractmethod

class CandidateRepository(ABC):
    @abstractmethod
    def get_corporations_by_id_election(id_electoral_process: str):
        ...
