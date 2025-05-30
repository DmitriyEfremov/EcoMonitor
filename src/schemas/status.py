from pydantic import BaseModel


class StatusBase(BaseModel):
    name: str
    is_final: bool


class StatusCreate(StatusBase):
    pass


class StatusRead(StatusBase):
    id: int

    class Config:
        orm_mode = True


class StatusUpdate(StatusBase):
    pass
