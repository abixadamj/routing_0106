import fastapi
from fastapi import Response, status

router = fastapi.APIRouter()

@router.get("/test_email/{email_to}")
def test_email_to(email_to: str):
    return {"mailto": email_to}
