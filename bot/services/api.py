import aiohttp
import os


BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://backend:8000/api/v1",
)


async def create_user(
    telegram_id: int,
    username: str | None,
    first_name: str,
):
    async with aiohttp.ClientSession() as session:

        async with session.post(
            f"{BACKEND_URL}/users/",
            json={
                "telegram_id": telegram_id,
                "username": username,
                "first_name": first_name,
            },
        ) as response:

            return await response.json()