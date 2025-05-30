from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.db.connection import get_db
from src.repositories.type_incident import TypeIncidentRepository
from src.schemas.type_incident import (
    TypeIncidentCreate,
    TypeIncidentRead,
    TypeIncidentUpdate,
)
from src.scripts.jwt import auth_schema
from src.scripts.role_checker import RoleChecker

router_type_incidents = APIRouter(
    prefix="/type_incidents",
    tags=["Type of incident CRUD"]
)


@router_type_incidents.post(
    "/create",
    response_model=TypeIncidentRead,
    status_code=status.HTTP_201_CREATED
)
async def create_type_incident(
        to_create: TypeIncidentCreate,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["manager", "admin"]))
) -> TypeIncidentRead:
    return await TypeIncidentRepository.create_type_incident(to_create, db)


@router_type_incidents.get(
    "/",
    response_model=list[TypeIncidentRead]
)
async def read_type_incidents(
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["user", "manager", "admin"]))
) -> list[TypeIncidentRead]:
    return await TypeIncidentRepository.read_type_incidents(db)


@router_type_incidents.get(
    "/{type_incident_id}",
    response_model=TypeIncidentRead
)
async def read_type_incident(
        type_incident_id: int,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["user", "manager", "admin"]))
) -> TypeIncidentRead:
    return await TypeIncidentRepository.read_type_incident(type_incident_id, db)


@router_type_incidents.put(
    "/update/{type_incident_id}",
    response_model=TypeIncidentUpdate
)
async def update_type_incident(
        type_incident_id:int,
        to_update: TypeIncidentUpdate,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["manager", "admin"]))
) -> TypeIncidentUpdate:
    return await TypeIncidentRepository.update_type_incident(
        type_incident_id,
        to_update,
        db)


@router_type_incidents.delete(
    "/delete/{type_incident_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_type_incident(
        type_incident_id: int,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["manager", "admin"]))
) -> None:
    await TypeIncidentRepository.delete_type_incident(type_incident_id, db)
