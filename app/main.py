import os

import dotenv

dotenv.load_dotenv()

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from database import models
from database.db import engine
from routers import messages, subscriptions, email_messages, gallery

models.Base.metadata.create_all(bind=engine)

origins = [os.getenv("CORS_ORIGIN_SERVER")]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

prefix = "/api/v1"

app.include_router(router=messages.router, prefix=prefix)
app.include_router(router=subscriptions.router, prefix=prefix)
app.include_router(router=email_messages.router, prefix=prefix)
app.include_router(router=gallery.router, prefix=prefix)
