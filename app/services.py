import httpx
from fastapi import HTTPException

from app.schemas import UserData


def get_user_data(user_id: int) -> UserData:
    response = httpx.get(f"https://reqres.in/api/users/{user_id}")
    user = response.json().get("data")

    if user:
        user_data = UserData(**user)
    else:
        raise HTTPException(status_code=404, detail="User not found")

    return user_data
