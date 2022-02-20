import fastapi
from emails.email_functions import mail_report
from emails.email_validation import validate_my_email
from fastapi import Response, status, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class MailSpec(BaseModel):
    mail_from: str
    mail_to: str
    mail_body: str



router = fastapi.APIRouter()

passwords = {
    "adasiek": "qwerty1234",
    "adamj": "7f19a0a0c9b0a2d7fd04c07e8aa57f08",
}


@router.get("/test_email/{email_to}", tags=["emails", "aaa"])
async def test_email_to(email_to: str, response: Response):
    if validate_my_email(email_to):
        # mail_message = f"Mail_spec {email_to} is OK"
        response.status_code = status.HTTP_202_ACCEPTED
    else:
        # mail_message = f"Mail_spec {email_to} is BAD"
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
    return {"mailto": email_to}


@router.put("/send_email/{email_to}", tags=["emails", "sending email"])
async def send_email_to(email_to: str, email_from: str, request: Request, response: Response,
                        email_body: str = "Welcome."):
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

    if mail_report(email_to, email_from, email_body):
        return Response(status_code=status.HTTP_201_CREATED)
    else:
        return Response(status_code=status.HTTP_502_BAD_GATEWAY)


@router.put("/send_email_header/", tags=["emails", "sending email"])
async def send_email_to_h(request: Request):
    """Authentication via X-Header : 'auth_id' """

    email_to = request.headers.get("email_to", "XXXX")
    email_from = request.headers.get("email_from", "XXXX")
    email_body = request.headers.get("email_body", "XXXX")
    auth_id = request.headers.get("auth_id", "XXXX")
    auth_password = request.headers.get("auth_password", "XXXX")

    if auth_id == "XXXX" or auth_password == "XXXX":
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        if passwords[auth_id] != auth_password:
            return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    if email_body == "XXXX":
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    mail_ok, report = mail_report(email_to, email_from, email_body)
    if mail_ok:
        return Response(status_code=status.HTTP_201_CREATED)
    else:
        json_compatible_item_data = jsonable_encoder(report)
        return JSONResponse(status_code=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS,
                            content=json_compatible_item_data)


@router.post("/send_email_body/", tags=["emails", "sending email"])
async def send_email_to_h(mail: MailSpec, request: Request):
    """Authentication via X-Header : 'auth_id'
    mail data via body request (JSON type schema)
    """

    auth_id = request.headers.get("auth_id", "XXXX")
    auth_password = request.headers.get("auth_password", "XXXX")

    if auth_id == "XXXX" or auth_password == "XXXX":
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        if passwords[auth_id] != auth_password:
            return Response(status_code=status.HTTP_401_UNAUTHORIZED)

    if not len(mail.mail_body):
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    mail_ok, report = mail_report(mail.mail_to, mail.mail_from, mail.mail_body)
    if mail_ok:
        return Response(status_code=status.HTTP_201_CREATED)
    else:
        json_compatible_item_data = jsonable_encoder(report)
        return JSONResponse(status_code=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS,
                            content=json_compatible_item_data)
