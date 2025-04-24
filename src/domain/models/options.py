from typing import Optional, List
from pydantic import BaseModel

class Options(BaseModel):
    sep: str
    low_memory: bool
    encoding: str
    header: Optional[bool] = None
    names: Optional[List[str]] = None
    dtype: Optional[dict[str, str]] = None