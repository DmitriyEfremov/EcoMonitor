from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from src.schemas.meta_file import FileMeta


class FileCreate(BaseModel):
    report_id: int
    user_id: UUID
    storage_id: UUID
    created_at: datetime


class FileReportRead(FileCreate):
    id: int

    class Config:
        orm_mode = True

class FileReportWithStorageRead(FileReportRead):
    storage: Optional[FileMeta]=None

class FileReportUpdate(FileReportRead):
    pass
