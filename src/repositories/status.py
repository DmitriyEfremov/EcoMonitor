from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status as starlette_status

from src.db.models import Status
from src.schemas.status import StatusCreate, StatusUpdate


class StatusRepository:
    @staticmethod
    async def create_status(
            to_create: StatusCreate,
            db: AsyncSession
    ) -> Status:
        new_status = Status(**to_create.dict())
        db.add(new_status)
        await db.commit()
        await db.refresh(new_status)
        return new_status

    @staticmethod
    async def read_statuses(db: AsyncSession) -> list[Status]:
        list_of_statuses = await db.execute(select(Status))
        result = list_of_statuses.scalars().all()
        return result

    @staticmethod
    async def read_status(
            status_id: int,
            db: AsyncSession
    ) -> Status:
        status_to_read = await db.execute(
            select(Status).where(Status.id == status_id)
        )
        result = status_to_read.scalar_one_or_none()
        if not result:
            raise HTTPException(
                status_code=starlette_status.HTTP_404_NOT_FOUND,
                detail="Статус не найдена"
            )
        return result

    @staticmethod
    async def update_status(
            status_id: int,
            to_update: StatusUpdate,
            db: AsyncSession
    ) -> Status:
        status_to_update = await db.execute(
            select(Status).where(Status.id == status_id)
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
    async def delete_status(
            status_id: int,
            db: AsyncSession
    ) -> None:
        status_to_delete = await db.execute(
            select(Status).where(Status.id == status_id)
        )
        result = status_to_delete.scalar_one_or_none()
        if not result:
            raise HTTPException(
                status_code=starlette_status.HTTP_404_NOT_FOUND,
                detail="Статус не найден"
            )
        await db.delete(result)
        await db.commit()
