import os
import random
from typing import Optional

from better_profanity import profanity
from fastapi import BackgroundTasks
from fastapi import HTTPException
from fastapi import status
from pydantic import BaseModel
from sendgrid.helpers.mail import Mail

from . import router
from helpers.messages_list import messages
from helpers.sendgrid_init import send_message


class EmailBase(BaseModel):
    year: Optional[int]

    class Config:
        orm_mode = True


class EmailToCouple(EmailBase):
    sender_name: str
    sender_message: str

    class Config:
        orm_mode = True


class EmailFromCouple(EmailBase):
    recipient_name: str
    recipient_email: str

    class Config:
        orm_mode = True


# End points
@router.post("/email/couple/from", status_code=status.HTTP_202_ACCEPTED)
async def send_email_from_couple(
    email_message: EmailFromCouple, background_task: BackgroundTasks
):
    message = Mail(
        from_email=os.getenv("FROM_EMAIL"),
        to_emails=email_message.recipient_email,
    )
    recipient_name = email_message.recipient_name
    year = email_message.year

    random_message = random.choice(messages)

    # Dynamic data in the templates
    message.dynamic_template_data = {
        "recipient_name": recipient_name.title(),
        "random_message": random_message,
        "year": year,
    }

    message.template_id = os.getenv("EMAIL_FROM_COUPLE_TEMPLATE")

    try:
        background_task.add_task(send_message, message)
        return status.HTTP_202_ACCEPTED
    except:
        raise HTTPException(
            status.HTTP_403_FORBIDDEN, detail="The email could not be sent"
        )


@router.post("/email/couple/to", status_code=status.HTTP_202_ACCEPTED)
async def send_email_to_couple(
    email_message: EmailToCouple, background_task: BackgroundTasks
):
    message = Mail(
        from_email=os.getenv("FROM_EMAIL"),
        to_emails=[os.getenv("EMAIL_GROOM"), os.getenv("EMAIL_BRIDE")],
    )

    sender_name = email_message.sender_name
    sender_message = profanity.censor(email_message.sender_message)
    year = email_message.year

    # Dynamic data in the templates
    message.dynamic_template_data = {
        "sender_name": sender_name.title(),
        "sender_message": sender_message,
        "year": year,
    }

    message.template_id = os.getenv("EMAIL_TO_COUPLE_TEMPLATE")

    try:
        background_task.add_task(send_message, message)
        return status.HTTP_202_ACCEPTED
    except Exception:
        raise HTTPException(
            status.HTTP_403_FORBIDDEN, detail="The email could not be sent"
        )
