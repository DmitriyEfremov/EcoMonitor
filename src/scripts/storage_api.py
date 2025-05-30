from uuid import UUID

import httpx
from fastapi import HTTPException, UploadFile
from fastapi.security import HTTPAuthorizationCredentials

from core.config import Settings


def get_thematic_bucket_id(entity_type: str) -> str:
    buckets = {
        "eco_problems": "0eaedc6b-bf10-4306-91a0-6944403c996e",
        "lost_founds": "0a31ea11-8d54-4d7b-b899-9bef33eb49e8",
    }
    return buckets.get(entity_type)


async def upload_to_storage(
        file: UploadFile, type_data_download: str, token: HTTPAuthorizationCredentials
) -> UUID:
    upload_url = f"{Settings.STORAGE_API}/api/v1/storage/upload_file"

    headers = {
        "Authorization": f"Bearer {token.credentials}",
    }

    files = {
        "file": (file.filename, file.file, file.content_type),
    }
    params = {
        "thematic_folder_id": type_data_download,
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                upload_url,
                headers=headers,
                files=files,
                params=params,
            )

            if response.status_code == 200:
                result = response.json()
                return result["storage_id"]
            error = response.text
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Failed to upload file: {error}"
            )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Request to StorageAPI failed: {str(e)}"
        ) from e


async def get_storage(storage_id: str,
                            token: HTTPAuthorizationCredentials) -> dict:
    metadata_url = f"{Settings.STORAGE_API}/api/v1/storage/{storage_id}"

    headers = {
        "Authorization": f"Bearer {token.credentials}",
    }
    params = {
        "storage_id": storage_id,
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(metadata_url,
                                        headers=headers,
                                        params=params)

            if response.status_code == 200:
                return response.json()
            error = response.text
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Failed to fetch file metadata: {error}"
            )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Request to StorageAPI failed: {str(e)}"
        ) from e
