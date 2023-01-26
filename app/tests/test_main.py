from fastapi.testclient import TestClient
import httpx
import respx

from app.main import app
from app.constants import BASE_API_URL


class TestMain:
    client = TestClient(app)

    @respx.mock
    def test_user_api(self, respx_mock):
        respx_mock.get(f"{BASE_API_URL}/3").mock(
            return_value=httpx.Response(
                200,
                json={
                    "data": {
                        "id": 3,
                        "first_name": "Ryan",
                        "last_name": "Flanagan",
                        "email": "ryan@example.com",
                        "avatar": "test.jpg",
                    }
                },
            ),
        )

        response = self.client.get("/user/3")
        assert response.status_code == 200
        assert response.json() == {
            "id": 3,
            "first_name": "Ryan",
            "last_name": "Flanagan",
            "email": "ryan@example.com",
            "avatar": "test.jpg",
        }

    @respx.mock
    def test_user_api_not_found(self, respx_mock):
        respx_mock.get(f"{BASE_API_URL}/100").mock(
            return_value=httpx.Response(
                404,
                json={},
            ),
        )

        response = self.client.get("/user/100")
        assert response.status_code == 404
        assert response.json() == {"detail": "User not found"}
