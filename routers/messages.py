from better_profanity import profanity
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import get_db
from . import router
from database.models import Message
from helpers.pastel_colors import return_random_color


class CreateMessageBase(BaseModel):
    name: str
    email: str
    message: str

    class Config:
        orm_mode = True


# Endpoints
@router.post("/message/create", status_code=status.HTTP_201_CREATED)
async def post_new_message(
    message: CreateMessageBase, db: Session = Depends(get_db)
):
    message.name = profanity.censor(message.name)
    message.message = profanity.censor(message.message)

    new_Message = Message(
        name=message.name.title(), email=message.email, message=message.message
    )

    try:
        db.add(new_Message)
        db.commit()

        return status.HTTP_201_CREATED
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Could not post the message",
        )


@router.get("/messages/all", status_code=status.HTTP_200_OK)
async def get_all_messages(db: Session = Depends(get_db)):
    try:
        all_messages = []
        single_message = {}
        records = db.query(Message).order_by(Message.date_created.desc()).all()

        if not records:
            return []

        for record in records:

            single_message["name"] = record.name
            single_message["email"] = record.email
            single_message["message"] = record.message
            single_message["color"] = return_random_color()

            all_messages.append(single_message.copy())

        return all_messages
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not fetch all the messages",
        )
