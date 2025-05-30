from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from src.schemas.meta_file import FileMeta


class FileCreate(BaseModel):
    eco_problem_id: int
    user_id: UUID
    storage_id: UUID
    created_at: datetime


class FileEcoRead(FileCreate):
    id: int

    class Config:
        orm_mode = True

class FileEcoWithStorageRead(FileEcoRead):
    storage: Optional[FileMeta]=None

class FileUpdate(FileEcoRead):
    pass
