from abc import ABC, abstractmethod
from src.domain.models.options import Options

class Extract(ABC):
    @abstractmethod
    def extract_from_file(self, path: str, options: Options):
        pass