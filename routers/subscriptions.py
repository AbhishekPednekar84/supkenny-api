from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from . import get_db
from . import router
from database.models import Subscription


# Check if user has previously subscribed
def check_if_email_exists(email: str, db: Session = Depends(get_db)):
    return db.query(Subscription).filter(Subscription.email == email).first()


# End points
@router.post("/subscribe/{email}", status_code=status.HTTP_201_CREATED)
async def subscribe_to_notifications(email: str, db: Session = Depends(get_db)):
    subscription = check_if_email_exists(email, db)

    if subscription:
        return {"message": "Looks like you have already subscribed!"}

    new_subscription = Subscription(email=email)

    try:
        db.add(new_subscription)
        db.commit()

        return {
            "message": "Thanks for subscribing! We will send you an email notification few days before the event."
        }
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Subscription failed",
        )
