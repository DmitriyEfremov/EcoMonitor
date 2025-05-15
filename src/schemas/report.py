from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from src.schemas.file_report import FileReportRead, FileReportWithStorageRead


class ReportBase(BaseModel):
    user_id: UUID
    title: str
    description: str
    status: int
    created_at: datetime

class ReportUpdate(ReportBase):
    manager_id: Optional[UUID]
    updated_at: datetime
    duplicate_task_id: Optional[int] = None


class ReportRead(ReportUpdate):
    id: int

    class Config:
        orm_mode = True


class ReportWithFileRead(ReportRead):
    files: Optional[list[FileReportRead]] = None

class ReportWithFileStorageRead(ReportRead):
    files: Optional[list[FileReportWithStorageRead]] = None

class ReportCreate(ReportBase):
    pass
