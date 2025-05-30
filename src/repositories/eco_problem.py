from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from starlette import status as starlette_status

from src.db.models import EcoProblem
from src.schemas.eco_problem import EcoProblemCreate, EcoProblemUpdate


class EcoProblemRepository:

    @staticmethod
    async def read_eco_problem_no_file(
            eco_problem_id: int,
            db: AsyncSession
    ) -> EcoProblem:
        eco_problem_to_read = await db.execute(
            select(EcoProblem)
            .where(EcoProblem.id == eco_problem_id)
        )
        result = eco_problem_to_read.unique().scalar_one_or_none()
        if not result:
            raise HTTPException(
                status_code=starlette_status.HTTP_404_NOT_FOUND,
                detail="Эко проблема не найдена"
            )
        return result

    @staticmethod
    async def create_eco_problem(
            to_create: EcoProblemCreate,
            db: AsyncSession
    ) -> EcoProblem:
        new_eco_problem = EcoProblem(**to_create.dict())
        new_eco_problem.files = []
        db.add(new_eco_problem)
        await db.commit()
        await db.refresh(new_eco_problem)
        return new_eco_problem

    @staticmethod
    async def read_eco_problems(db: AsyncSession) -> list[EcoProblem]:
        statement =  (select(EcoProblem)
                    .options(joinedload(EcoProblem.files))
                      )
        list_of_eco_problems = await db.execute(statement)
        result = list_of_eco_problems.unique().scalars().all()
        return result

    @staticmethod
    async def read_eco_problem(
            eco_problem_id: int,
            db: AsyncSession
    ) -> EcoProblem:
        eco_problem_to_read = await db.execute(
            select(EcoProblem)
            .where(EcoProblem.id == eco_problem_id)
            .options(joinedload(EcoProblem.files))
        )
        result = eco_problem_to_read.unique().scalar_one_or_none()
        if not result:
            raise HTTPException(
                status_code=starlette_status.HTTP_404_NOT_FOUND,
                detail="Эко проблема не найдена"
            )
        return result

    @staticmethod
    async def update_eco_problem(
            eco_problem_id:int,
            to_update: EcoProblemUpdate,
            db: AsyncSession
    ) -> EcoProblem:
        result = await EcoProblemRepository.read_eco_problem_no_file(
            eco_problem_id,
            db
        )
        for key, value in to_update.dict().items():
            setattr(result, key, value)
        await db.commit()
        await db.refresh(result)
        return result

    @staticmethod
    async def update_eco_problem_status(
            eco_problem_id: int,
            status_id: int,
            db: AsyncSession) -> EcoProblem:
        result = await EcoProblemRepository.read_eco_problem_no_file(
            eco_problem_id,
            db
        )
        result.status_id = status_id
        await db.commit()
        await db.refresh(result)
        return result

    @staticmethod
    async def update_eco_problem_manager(
            eco_problem_id: int,
            manager_id: UUID,
            db: AsyncSession
    ) -> EcoProblem:
        result = await EcoProblemRepository.read_eco_problem_no_file(
            eco_problem_id,
            db
        )
        result.manager_id = manager_id
        await db.commit()
        await db.refresh(result)
        return result

    @staticmethod
    async def close_eco_problem(
            eco_problem_id: int,
            db: AsyncSession
    ) -> EcoProblem:
        result = await EcoProblemRepository.read_eco_problem_no_file(
            eco_problem_id,
            db
        )
        result.is_closed = True
        await db.commit()
        await db.refresh(result)
        return result

    @staticmethod
    async def delete_eco_problem(eco_problem_id: int, db: AsyncSession) -> None:
        result = await EcoProblemRepository.read_eco_problem_no_file(
            eco_problem_id,
            db
        )
        await db.delete(result)
        await db.commit()
