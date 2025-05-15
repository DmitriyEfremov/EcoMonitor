from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from src.schemas.file_eco import FileEcoRead, FileEcoWithStorageRead


class EcoProblemBase(BaseModel):
    creator_id: UUID
    manager_id: UUID
    title: str
    description: str
    status_id: int
    type_incident_id: int
    longitude: str
    latitude: str
    is_closed: bool = False


class EcoProblemRead(EcoProblemBase):
    id:int

    class Config:
        orm_mode = True

class EcoProblemWithFileRead(EcoProblemRead):
    files: Optional[list[FileEcoRead]] = []

class EcoProblemWithFileStorageRead(EcoProblemRead):
    files: Optional[list[FileEcoWithStorageRead]] = []

class EcoProblemUpdate(EcoProblemBase):
    pass


class EcoProblemCreate(EcoProblemBase):
    pass
