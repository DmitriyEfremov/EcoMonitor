from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status as starlette_status

from src.db.models import FileEcoProblem


class FileEcoRepository:
    @staticmethod
    async def create_file(
            eco_problem_id: int,
            user: UUID,
            storage_id: UUID,
            db: AsyncSession
    ) -> FileEcoProblem:
        new_file = FileEcoProblem()
        new_file.user_id = user
        new_file.eco_problem_id = eco_problem_id
        new_file.storage_id = storage_id
        db.add(new_file)
        await db.commit()
        await db.refresh(new_file)
        return new_file

    @staticmethod
    async def read_files(db: AsyncSession) -> list[FileEcoProblem]:
        list_of_files = await db.execute(select(FileEcoProblem))
        result = list_of_files.scalars().all()
        return result

    @staticmethod
    async def read_file(
            file_id: int,
            db: AsyncSession
    ) -> FileEcoProblem:
        file_to_read = await db.execute(
            select(FileEcoProblem).where(FileEcoProblem.id == file_id)
        )
        result = file_to_read.scalar_one_or_none()
        if not result:
            raise HTTPException(
                status_code=starlette_status.HTTP_404_NOT_FOUND,
                detail="Файл не найдена"
            )
        return result

    @staticmethod
    async def add_file_to_eco_problem(
            eco_problem_id: int,
            user:UUID,
            files: list[UUID],
            db: AsyncSession) -> list[FileEcoProblem]:
        res_list = []
        for f in files:
            res_list.append(await FileEcoRepository.create_file(
                eco_problem_id,
                user,
                f,
                db
            ))
        await db.commit()
        return res_list

    @staticmethod
    async def delete_file(
            file_id: int,
            db: AsyncSession
    ) -> None:
        file_to_delete = await db.execute(
            select(FileEcoProblem).where(FileEcoProblem.id == file_id)
        )
        result = file_to_delete.scalar_one_or_none()
        if not result:
            raise HTTPException(
                status_code=starlette_status.HTTP_404_NOT_FOUND,
                detail="Файл не найдена"
            )
        await db.delete(result)
        await db.commit()
