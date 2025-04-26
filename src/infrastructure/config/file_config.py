from dataclasses import dataclass
import os
from datetime import datetime
from pathlib import Path

@dataclass
class FileConfig:
    base_dir: str = "data"
    temp_dir: str = "temp"
    uploads_dir: str = "uploads"

    def __post_init__(self):
        """Asegura que los directorios existan."""
        # Convertir rutas relativas a absolutas
        self.base_dir = os.path.abspath(self.base_dir)
        self.temp_dir = os.path.join(self.base_dir, self.temp_dir)
        self.uploads_dir = os.path.join(self.base_dir, self.uploads_dir)
        
        # Crear directorios
        self._ensure_directories()

    def _ensure_directories(self) -> None:
        """Crea los directorios necesarios si no existen."""
        for directory in [self.base_dir, self.temp_dir, self.uploads_dir]:
            os.makedirs(directory, exist_ok=True)

    def get_temp_path(self) -> str:
        """Obtiene la ruta completa del directorio temporal."""
        return self.temp_dir

    def get_uploads_path(self) -> str:
        """Obtiene la ruta completa del directorio de uploads."""
        return self.uploads_dir

    def generate_filename(self, original_filename: str) -> str:
        """
        Genera un nombre de archivo con el formato DMY_HM_μs.extension
        
        Args:
            original_filename: Nombre original del archivo
            
        Returns:
            str: Nuevo nombre de archivo
        """
        # Obtener la extensión del archivo original
        extension = os.path.splitext(original_filename)[1]
        
        # Generar timestamp con el formato requerido
        timestamp = datetime.now().strftime("%d%m%Y_%H%M_%f")
        
        return f"{timestamp}{extension}" 