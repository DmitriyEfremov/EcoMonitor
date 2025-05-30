from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status as starlette_status

from src.db.models import TypeIncident
from src.schemas.type_incident import TypeIncidentCreate, TypeIncidentUpdate


class TypeIncidentRepository:
    @staticmethod
    async def create_type_incident(
            to_create: TypeIncidentCreate,
            db: AsyncSession
    ) -> TypeIncident:
        new_type_incident = TypeIncident(**to_create.dict())
        db.add(new_type_incident)
        await db.commit()
        await db.refresh(new_type_incident)
        return new_type_incident

    @staticmethod
    async def read_type_incidents(db: AsyncSession) -> list[TypeIncident]:
        list_of_types = await db.execute(select(TypeIncident))
        result = list_of_types.scalars().all()
        return result

    @staticmethod
    async def read_type_incident(
            type_incident_id: int,
            db: AsyncSession
    ) -> TypeIncident:
        type_to_read = await db.execute(
            select(TypeIncident).where(TypeIncident.id == type_incident_id)
        )
        result = type_to_read.scalar_one_or_none()
        if not result:
            raise HTTPException(
                status_code=starlette_status.HTTP_404_NOT_FOUND,
                detail="Тип инцидента не найдена"
            )
        return result

    @staticmethod
    async def update_type_incident(
            type_incident_id: int,
            to_update: TypeIncidentUpdate,
            db: AsyncSession
    ) -> TypeIncident:
        type_to_update = await db.execute(
            select(TypeIncident).where(TypeIncident.id == type_incident_id)
        )
        result = type_to_update.scalar_one_or_none()
        if not result:
            raise HTTPException(
                status_code=starlette_status.HTTP_404_NOT_FOUND,
                detail="Тип инцидента не найдена"
            )
        for key, value in to_update.dict().items():
            setattr(result, key, value)
        await db.commit()
        await db.refresh(result)
        return result

    @staticmethod
    async def delete_type_incident(
            type_incident_id: int,
            db: AsyncSession
    ) -> None:
        status_to_delete = await db.execute(
            select(TypeIncident).where(TypeIncident.id == type_incident_id)
        )
        result = status_to_delete.scalar_one_or_none()
        if not result:
            raise HTTPException(
                status_code=starlette_status.HTTP_404_NOT_FOUND,
                detail="Статус не найден"
            )
        await db.delete(result)
        await db.commit()
