# from fastapi import APIRouter

# router = APIRouter(prefix="/users", tags=["Users"])


# @router.get("/")
# async def get_users():
#     return {
#         "users": [
#             {"id": 1, "name": "Rashmitha"},
#             {"id": 2, "name": "Developer"}
#         ]
#     }


from fastapi import APIRouter, Depends
from app.dependencies.auth import verify_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def get_users(user=Depends(verify_user)):
    return {
        "status": user,
        "users": [
            {"id": 1, "name": "Rashmitha"},
            {"id": 2, "name": "Developer"}
        ]
    }