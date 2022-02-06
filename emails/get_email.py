import fastapi
from emails.email_functions import mail_report
from emails.email_validation import validate_my_email
from fastapi import Response, status, Request

router = fastapi.APIRouter()

passwords = {
    "adasiek": "qwerty1234",
    "adamj": "7f19a0a0c9b0a2d7fd04c07e8aa57f08",
}

@router.get("/test_email/{email_to}", tags=["emails", "aaa"])
async def test_email_to(email_to: str, response: Response):
    if validate_my_email(email_to):
        # mail_message = f"Mail {email_to} is OK"
        response.status_code = status.HTTP_202_ACCEPTED
    else:
        # mail_message = f"Mail {email_to} is BAD"
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
    return {"mailto": email_to}


@router.put("/send_email/{email_to}", tags=["emails", "sending email"])
async def send_email_to(email_to: str, request: Request, response: Response, email_body: str = "Welcome."):
    """Authentication via X-Header : 'auth_id' """

    auth_id = request.headers.get("auth_id", "XXXX")
    auth_password = request.headers.get("auth_password", "XXXX")

    if auth_id == "XXXX" or auth_password == "XXXX":
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        if passwords[auth_id] != auth_password:
            return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    if email_body == " ":
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    if mail_report(email_to, email_body):
        return Response(status_code=status.HTTP_201_CREATED)
    else:
        return Response(status_code=status.HTTP_502_BAD_GATEWAY)





