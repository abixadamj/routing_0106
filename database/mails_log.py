# to-do:
# sqlite access with pydantic model
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()


class MailData(BaseModel):
    mail_id: str
    mail_from: str
    mail_to: str
    """next - we will add some user's data: login etc.."""


@router.put("/sendmail_session/", tags=["sendmail_sessions"])
async def save_sendmail_session(mail_data: MailData) -> str:
    """save log about sending mail to database
    auth via cookies or something similar
    :returns message string ID stored in database"""
    pass


@router.get("/sendmail_sessions", tags=["sendmail_sessions"])
async def get_sendmail_sessions() -> list:
    """
    auth via cookies or something similar
    :returns list of messages string IDs
    """
    pass


@router.get("/sendmail_session/{session_id}", tags=["sendmail_sessions"])
async def get_sendmail_session(session_id: str) -> dict:
    """
    auth via cookies or something similar
    :returns details of message for given string IDs
    """
    pass
