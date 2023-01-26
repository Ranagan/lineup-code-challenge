import httpx
import pytest
import respx
from fastapi import HTTPException

from app.constants import BASE_API_URL
from app.schemas import UserData
from app.services import get_user_data


class TestGetUserService:
    @respx.mock
    def test_get_data(self, respx_mock):
        respx_mock.get(f"{BASE_API_URL}/1").mock(
            return_value=httpx.Response(
                200,
                json={
                    "data": {
                        "id": 1,
                        "first_name": "Ryan",
                        "last_name": "Flanagan",
                        "email": "ryan@example.com",
                        "avatar": "test.jpg",
                    }
                },
            ),
        )

        expected = UserData(
            id=1,
            first_name="Ryan",
            last_name="Flanagan",
            email="ryan@example.com",
            avatar="test.jpg",
        )
        result = get_user_data(1)

        assert result == expected

    @respx.mock
    def test_raises_404(self, respx_mock):
        respx_mock.get(f"{BASE_API_URL}/100").mock(
            return_value=httpx.Response(404, json={}),
        )

        with pytest.raises(HTTPException) as exc:
            result = get_user_data(100)

        assert exc.value.status_code == 404
        assert exc.value.detail == "User not found"
