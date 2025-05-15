from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from starlette import status as starlette_status

from src.db.models import Report
from src.schemas.report import ReportCreate, ReportUpdate


class ReportRepository:


    @staticmethod
    async def read_report_no_file(
            read_id: id,
            db: AsyncSession
    ) -> Report:
        report = await db.execute(
            select(Report)
            .where(Report.id == read_id)
        )
        result = report.unique().scalar_one_or_none()
        if not result:
            raise HTTPException(
                status_code=starlette_status.HTTP_404_NOT_FOUND,
                detail="Обращение не найдено"
            )
        return result


    @staticmethod
    async def create_report(
            to_create: ReportCreate,
            db: AsyncSession
    ) -> Report:
        new_report = Report(**to_create.dict())
        new_report.files=[]
        db.add(new_report)
        await db.commit()
        await db.refresh(new_report)
        return new_report

    @staticmethod
    async def read_reports(db: AsyncSession) ->list[Report]:
        all_reports = await db.execute(
            select(Report)
            .options(joinedload(Report.files)))
        result = all_reports.unique().scalars().all()
        return result


    @staticmethod
    async def read_report(
            read_id: id,
            db: AsyncSession
    ) -> Report:
        report = await db.execute(
            select(Report)
            .where(Report.id == read_id)
            .options(joinedload(Report.files))
        )
        result = report.unique().scalar_one_or_none()
        if not result:
            raise HTTPException(
                status_code=starlette_status.HTTP_404_NOT_FOUND,
                detail="Обращение не найдено"
            )
        return result


    @staticmethod
    async def update_report(
            report_id:int,
            to_update: ReportUpdate,
            db: AsyncSession
    ) -> Report:
        result = await ReportRepository.read_report_no_file(
            report_id,
            db
        )
        for key, value in to_update.dict().items():
            setattr(result, key, value)
        await db.commit()
        await db.refresh(result)
        return result

    @staticmethod
    async def update_status_report(
            report_id: int,
            new_status: str,
            db: AsyncSession
    ) -> Report:
        result = await ReportRepository.read_report_no_file(
            report_id,
            db
        )
        setattr(result, new_status, True)
        await db.commit()
        await db.refresh(result)
        return result

    @staticmethod
    async def delete_report(
            report_id: int,
            db: AsyncSession
    ) -> None:
        result = await ReportRepository.read_report_no_file(
            report_id,
            db
        )
        await db.delete(result)
        await db.commit()
