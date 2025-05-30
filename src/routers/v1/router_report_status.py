from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.db.connection import get_db
from src.repositories.report_status import ReportStatusRepository
from src.schemas.report_status import (
    ReportStatusCreate,
    ReportStatusRead,
    ReportStatusUpdate,
)

auth_schema = HTTPBearer()

router_report_status = APIRouter(prefix="/report_statuses", tags=["Report_Status"])


@router_report_status.post("/create", response_model=ReportStatusRead)
async def create_report_status(
        to_create: ReportStatusCreate,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema)
) -> ReportStatusCreate:
    return await ReportStatusRepository.create_report_status(to_create, db)


@router_report_status.get("/", response_model=list[ReportStatusRead])
async def read_report_statuses(
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema)
) ->list[ReportStatusRead]:
    return await ReportStatusRepository.read_report_statuses(db)


@router_report_status.get("/{report_status_id}",
                          response_model=ReportStatusRead)
async def read_report_status(
        read_id: int,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema)
) ->ReportStatusRead:
    return await ReportStatusRepository.read_report_status(read_id, db)


@router_report_status.put("/update/{report_status_id}",
                          response_model=ReportStatusUpdate)
async def update_report_status(
        report_status_id: int,
        to_update: ReportStatusUpdate,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema)
) -> ReportStatusUpdate:
    return await ReportStatusRepository.update_report_status(
        report_status_id,
        to_update,
        db)


@router_report_status.delete("/delete/{report_status_id}",
                      status_code=status.HTTP_204_NO_CONTENT)
async def delete_report_status(
        delete_id: int,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema)
) -> None:
    return await ReportStatusRepository.delete_report_status(delete_id, db)
