from dataclasses import dataclass
from typing import Optional
import os
from dotenv import load_dotenv

@dataclass
class DatabaseConfig:
    host: str
    port: int
    database: str
    user: str
    password: str
    schema: str = "kits_electorales"

    @property
    def connection_string(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

    @classmethod
    def from_env(cls) -> 'DatabaseConfig':
        load_dotenv()

        return cls(
            host=os.getenv('DB_HOST', 'localhost'),
            port=int(os.getenv('DB_PORT', '5433')),
            database=os.getenv('DB_NAME', 'kits_electorales'),
            user=os.getenv('DB_USER', 'postgres'),
            password=os.getenv('DB_PASSWORD', '1234'),
            schema=os.getenv('DB_SCHEMA', 'kits_electorales')
        )

    @classmethod
    def from_dict(cls, config_dict: dict) -> 'DatabaseConfig':
        return cls(
            host=config_dict.get('host', 'localhost'),
            port=int(config_dict.get('port', 5433)),
            database=config_dict.get('database', 'kits_electorales'),
            user=config_dict.get('user', 'postgres'),
            password=config_dict.get('password', '1234'),
            schema=config_dict.get('schema', 'kits_electorales')
        ) 