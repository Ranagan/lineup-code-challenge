from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services import get_user_data


app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(CORSMiddleware, allow_origins=origins)


@app.get("/user/{user_id}/")
def user_api(user_id: int):
    return get_user_data(user_id)
