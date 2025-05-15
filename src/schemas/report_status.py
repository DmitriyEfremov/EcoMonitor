from pydantic import BaseModel


class ReportStatusBase(BaseModel):
    name: str
    is_final: bool


class ReportStatusCreate(ReportStatusBase):
    pass


class ReportStatusRead(ReportStatusBase):
    id: int

    class Config:
        orm_mode = True


class ReportStatusUpdate(ReportStatusBase):
    pass
