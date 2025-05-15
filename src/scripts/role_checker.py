from fastapi import Depends, HTTPException
from starlette import status

from src.scripts.jwt import get_role


class RoleChecker:
    def __init__(self, required_role: list[str]) -> None:
        self.required_role = required_role

    def __call__(self, role: str = Depends(get_role)) -> bool:
        if role not in self.required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="The user does not have access to the resource"
            )
        return True
