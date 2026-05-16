from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def get_users():
    return {
        "users": [
            {"id": 1, "name": "Rashmitha"},
            {"id": 2, "name": "Developer"}
        ]
    }