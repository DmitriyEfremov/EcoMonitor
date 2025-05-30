from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from core.logger import logger
from src.db.connection import get_db
from src.repositories.eco_problem import EcoProblemRepository
from src.schemas.eco_problem import (
    EcoProblemCreate,
    EcoProblemRead,
    EcoProblemUpdate,
    EcoProblemWithFileStorageRead,
)
from src.schemas.file_eco import FileEcoWithStorageRead
from src.schemas.meta_file import FileMeta
from src.scripts.jwt import auth_schema
from src.scripts.role_checker import RoleChecker
from src.scripts.storage_api import get_storage

router_eco_problems = APIRouter(prefix="/eco_problems", tags=["Eco problem CRUD"])


@router_eco_problems.post(
    "/create",
    response_model = EcoProblemRead,
    status_code=status.HTTP_201_CREATED
)
async def create_eco_problem(
        to_create: EcoProblemCreate,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["user", "manager", "admin"]))
) -> EcoProblemRead:
    return await EcoProblemRepository.create_eco_problem(to_create, db)


@router_eco_problems.get(
    "/",
    response_model=list[EcoProblemRead]
)
async def read_eco_problems(
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["user", "manager", "admin"]))
) -> list[EcoProblemRead]:
    eco_problems = await EcoProblemRepository.read_eco_problems(db)
    return eco_problems


@router_eco_problems.get(
    "/{eco_problem_id}",
    response_model=EcoProblemWithFileStorageRead
)
async def read_eco_problem(
        eco_problem_id: int,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["user", "manager", "admin"]))
) -> EcoProblemWithFileStorageRead:
    eco = await EcoProblemRepository.read_eco_problem(eco_problem_id, db)
    try:
        files=[]
        for file_eco in eco.files:
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
            file_to_add = FileEcoWithStorageRead(
                eco_problem_id=file_eco.eco_problem_id,
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
            eco.id, e.detail
        )
        files=[]

    #
        # Создаем объект ContentRead с мета-информацией
    content_dict = eco.__dict__
    content_dict["files"]=files
    return EcoProblemWithFileStorageRead(**content_dict)
    # return storage


@router_eco_problems.put(
    "/update/{eco_problem_id}",
    response_model=EcoProblemRead
)
async def update_eco_problem(
        eco_problem_id:int,
        to_update: EcoProblemUpdate,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["user", "manager", "admin"]))
) -> EcoProblemRead:
    return await EcoProblemRepository.update_eco_problem(eco_problem_id,to_update, db)


@router_eco_problems.patch(
    "/update-status/{eco_problem_id}",
    response_model=EcoProblemRead
)
async def update_eco_problem_status(
        eco_problem_id: int,
        status_id: int,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["manager", "admin"]))
) -> EcoProblemRead:
    return await EcoProblemRepository.update_eco_problem_status(
        eco_problem_id=eco_problem_id,
        status_id=status_id,
        db=db
    )

@router_eco_problems.patch("/update-manager/{eco_problem_id}")
async def update_eco_problem_manager(
        eco_problem_id: int,
        manager_id: UUID,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["user", "manager", "admin"]))
) -> EcoProblemRead:
    return await EcoProblemRepository.update_eco_problem_manager(
        eco_problem_id=eco_problem_id,
        manager_id=manager_id,
        db=db
    )


@router_eco_problems.patch("/close-eco-problem/{eco_problem_id}")
async def close_eco_problem(
        eco_problem_id: int,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["manager", "admin"]))
) -> EcoProblemRead:
    return await EcoProblemRepository.close_eco_problem(eco_problem_id, db)


@router_eco_problems.delete(
    "/delete/{eco_problem_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_eco_problem(
        eco_problem_id: int,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["manager", "admin"]))
) -> None:
    await EcoProblemRepository.delete_eco_problem(eco_problem_id, db)
