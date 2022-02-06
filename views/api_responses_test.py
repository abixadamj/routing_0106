import fastapi
from fastapi import Response, status

router = fastapi.APIRouter()

our_users = {
    "adasiek": ["qwerty123", "Adam Jurkiewicz"],
    "beata": ["ytrewq321", "Beata Jurkiewicz"],
}


@router.get("/users/{user_id}")
async def user_list(user_id: str, response: Response, password: str = "NIC"):
    if user_id not in our_users:
        response.status_code = status.HTTP_404_NOT_FOUND
        return "None"
    else:
        user_info = our_users[user_id][1]
        stored_password = our_users[user_id][0]

        if stored_password != password:
            response.status_code = status.HTTP_401_UNAUTHORIZED
            return f"Bad password: {password}"

        response.status_code = status.HTTP_200_OK
        return {user_id: user_info }
