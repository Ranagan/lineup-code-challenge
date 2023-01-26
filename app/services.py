import httpx
from fastapi import HTTPException

from app.constants import BASE_API_URL
from app.schemas import UserData


def get_user_request(user_id: int):
    try:
        response = httpx.get(f"{BASE_API_URL}/{user_id}")

        data = response.json().get("data")
        return data
    except httpx.HTTPError as exc:
        raise exc


def get_user_data(user_id: int) -> UserData:
    user_data = get_user_request(user_id)

    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    return UserData(**user_data)
