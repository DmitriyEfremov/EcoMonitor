from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.db.connection import get_db
from src.repositories.status import StatusRepository
from src.schemas.status import StatusCreate, StatusRead, StatusUpdate
from src.scripts.jwt import auth_schema
from src.scripts.role_checker import RoleChecker

router_statuses = APIRouter(prefix="/statuses", tags=["Status CRUD"])


@router_statuses.post(
    "/create",
    response_model=StatusRead,
    status_code=status.HTTP_201_CREATED
)
async def create_status(
        to_create: StatusCreate,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["manager", "admin"]))
) -> StatusRead:
    return await StatusRepository.create_status(to_create, db)


@router_statuses.get(
    "/",
    response_model=list[StatusRead]
)
async def read_statuses(
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["user", "manager", "admin"]))
) -> list[StatusRead]:
    return await StatusRepository.read_statuses(db)


@router_statuses.get(
    "/{status_id}",
    response_model=StatusRead
)
async def read_status(
        status_id: int,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["user", "manager", "admin"]))
) -> StatusRead:
    return await StatusRepository.read_status(status_id, db)


@router_statuses.put(
    "/update-info",
    response_model=StatusUpdate
)
async def update_status(
        status_id:int,
        to_update: StatusUpdate,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["manager", "admin"]))
) -> StatusRead:
    return await StatusRepository.update_status(status_id, to_update, db)


@router_statuses.delete(
    "/delete/{status_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_status(
        status_id: int,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["manager", "admin"]))
) -> None:
    await StatusRepository.delete_status(status_id, db)
