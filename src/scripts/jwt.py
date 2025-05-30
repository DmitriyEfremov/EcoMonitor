from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from starlette import status

from core.config import Settings

auth_schema = HTTPBearer()


def get_payload(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            Settings.SECRET_KEY,
            algorithms=[Settings.ALGORITHM]
        )
        email = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        ) from e
    return payload


def get_role(token: HTTPAuthorizationCredentials = Depends(auth_schema)) -> str:
    try:
        payload = jwt.decode(
            token.credentials,
            Settings.SECRET_KEY,
            algorithms=[Settings.ALGORITHM]
        )
        email = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        ) from e
    return payload["role"]
