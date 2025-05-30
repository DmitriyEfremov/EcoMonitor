from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from core.logger import logger
from src.db.connection import get_db
from src.repositories.report import ReportRepository
from src.schemas.file_report import FileReportWithStorageRead
from src.schemas.meta_file import FileMeta
from src.schemas.report import (
    ReportCreate,
    ReportRead,
    ReportUpdate,
    ReportWithFileStorageRead,
)
from src.scripts.storage_api import get_storage

auth_schema = HTTPBearer()

router_report = APIRouter(prefix="/reports", tags=["Report CRUD"])


@router_report.post(
    "/create",
    response_model=ReportRead,
    status_code=status.HTTP_201_CREATED
)
async def create_report(
        to_create: ReportCreate,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
) -> ReportRead:
    return await ReportRepository.create_report(to_create, db)


@router_report.get(
    "/",
    response_model=list[ReportRead])
async def read_reports(
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema)
) ->list[ReportRead]:
    return await ReportRepository.read_reports(db)


@router_report.get(
    "/{report_id}",
    response_model=ReportWithFileStorageRead
)
async def read_report(
        read_id: int,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema)
) ->ReportWithFileStorageRead:
    report = await ReportRepository.read_report(read_id, db)
    try:
        files=[]
        for file_eco in report.files:
            data = await get_storage(
                    str(file_eco.storage_id), token
                )
            meta_data = FileMeta(
                creator_id=data["creator_id"],
                url=data["url"],
                created_at=data["created_at"],
                thematic_folder_id=data["thematic_folder_id"],
                id=data["id"]
            )

        # Получаем мета-информацию о файле из StorageAPI
            file_to_add = FileReportWithStorageRead(
                report_id=file_eco.report_id,
                created_at=file_eco.created_at,
                storage=meta_data,
                storage_id=file_eco.storage_id,
                user_id=file_eco.user_id,
                id=file_eco.id
            )

            files.append(file_to_add)

    except HTTPException as e:
        logger.error(
            "Failed to fetch file metadata for content %s: %s",
            report.id, e.detail
        )
        files=[]

    content_dict = report.__dict__
    content_dict["files"]=files
    return ReportWithFileStorageRead(**content_dict)


@router_report.put(
    "/update/{report_id}",
    response_model=ReportUpdate)
async def update_report(
        report_id: int,
        to_update: ReportUpdate,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema)
) -> ReportUpdate:
    return await ReportRepository.update_report(report_id, to_update, db)


@router_report.delete(
    "/delete/{report_id}",
    status_code=status.HTTP_204_NO_CONTENT)
async def delete_report(
        delete_id: int,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema)
) -> None:
    return await ReportRepository.delete_report(delete_id, db)
