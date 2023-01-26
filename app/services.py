import httpx
from schemas import UserData


def get_user_data(user_id: int) -> UserData:
    response = httpx.get(f"https://reqres.in/api/users/{user_id}")
    user = response.json()["data"]

    user_data = UserData(**user)

    return user_data
