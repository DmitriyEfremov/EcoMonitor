from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status as starlette_status

from src.db.models import ReportStatus
from src.schemas.report_status import ReportStatusCreate, ReportStatusUpdate


class ReportStatusRepository:
    @staticmethod
    async def create_report_status(
            to_create: ReportStatusCreate,
            db: AsyncSession
    ) -> ReportStatus:
        new_report_status = ReportStatus(**to_create.dict())
        db.add(new_report_status)
        await db.commit()
        await db.refresh(new_report_status)
        return new_report_status

    @staticmethod
    async def read_report_statuses(db: AsyncSession) -> list[ReportStatus]:
        list_of_report_statuses = await db.execute(select(ReportStatus))
        result = list_of_report_statuses.scalars().all()
        return result

    @staticmethod
    async def read_report_status(
            status_id: int,
            db: AsyncSession
    ) -> ReportStatus:
        status_to_read = await db.execute(
            select(ReportStatus).where(ReportStatus.id == status_id)
        )
        result = status_to_read.scalar_one_or_none()
        if not result:
            raise HTTPException(
                status_code=starlette_status.HTTP_404_NOT_FOUND,
                detail="Статус не найдена"
            )
        return result

    @staticmethod
    async def update_report_status(
            report_status_id:int,
            to_update: ReportStatusUpdate,
            db: AsyncSession
    ) -> ReportStatus:
        status_to_update = await db.execute(
            select(ReportStatus).where(ReportStatus.id == report_status_id)
        )
        result = status_to_update.scalar_one_or_none()
        if not result:
            raise HTTPException(
                status_code=starlette_status.HTTP_404_NOT_FOUND,
                detail="Статус не найдена"
            )

        for key, value in to_update.dict().items():
            setattr(result, key, value)
        await db.commit()
        await db.refresh(result)
        return result

    @staticmethod
    async def delete_report_status(
            status_id: int,
            db: AsyncSession
    ) -> None:
        status_to_delete = await db.execute(
            select(ReportStatus).where(ReportStatus.id == status_id)
        )
        result = status_to_delete.scalar_one_or_none()
        if not result:
            raise HTTPException(
                status_code=starlette_status.HTTP_404_NOT_FOUND,
                detail="Статус не найден"
            )
        await db.delete(result)
        await db.commit()
