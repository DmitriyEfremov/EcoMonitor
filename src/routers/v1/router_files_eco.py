import base64
import json

from fastapi import APIRouter, Depends, UploadFile
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.db.connection import get_db
from src.repositories.file_eco import FileEcoRepository
from src.schemas.file_eco import FileEcoRead
from src.scripts.jwt import auth_schema
from src.scripts.role_checker import RoleChecker
from src.scripts.storage_api import get_thematic_bucket_id, upload_to_storage

router_files_eco = APIRouter(prefix="/files_eco", tags=["File CRUD"])



@router_files_eco.post(
    "/upload-files",
    response_model = list[FileEcoRead]
)
async def add_file_to_eco_problem(
        eco_problem_id:int,
        files:list[UploadFile],
        db:AsyncSession = Depends(get_db),
    token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["user", "manager", "admin"]))
) -> list[FileEcoRead]:
    storage_ids = []
    bucket_id = get_thematic_bucket_id("eco_problems")
    # декодируем user_id из токена
    get_user = token.credentials
    parts = get_user.split(".")
    if len(parts) != 3:
        raise ValueError("Invalid JWT format")
    payload = parts[1]
    padding = len(payload) % 4
    if padding:
        payload += "=" * (4 - padding)
    try:
        payload = base64.b64decode(payload).decode("utf-8")
    except Exception as e:
        raise ValueError("Failed to decode JWT payload") from e
    try:
        payload = json.loads(payload)
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON in JWT payload") from e
    user = (payload.get("user_id")
            or payload.get("sub")
            or payload.get("uuid"))
    # загружаем все файлы в бакет
    for f in files:
        storage_id = await upload_to_storage(f, bucket_id, token)
        storage_ids.append(storage_id)
    return await FileEcoRepository.add_file_to_eco_problem(
        eco_problem_id,user,
        storage_ids,
        db
    )


@router_files_eco.get(
    "/",
    response_model=list[FileEcoRead]
)
async def read_files(
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["manager", "admin"]))
) -> list[FileEcoRead]:
    return await FileEcoRepository.read_files(db)


@router_files_eco.get(
    "/{file_id}",
    response_model=FileEcoRead
)
async def read_file(
        file_id: int,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["user", "manager", "admin"]))
) -> FileEcoRead:
    return await FileEcoRepository.read_file(file_id, db)


@router_files_eco.delete(
    "/delete/{file_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_file(
        file_id: int,
        db: AsyncSession = Depends(get_db),
        token: HTTPAuthorizationCredentials = Depends(auth_schema),
        _: bool = Depends(RoleChecker(required_role=["user", "manager", "admin"]))
) -> None:
    await FileEcoRepository.delete_file(file_id, db)
