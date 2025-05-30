from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class FileMeta(BaseModel):
    creator_id: UUID
    url: str
    created_at: datetime
    thematic_folder_id: UUID
    id: UUID
