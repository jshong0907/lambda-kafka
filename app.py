import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from schemas import InputSchema
from models import Log


def handler(event, context):
    input = InputSchema(**event)
    engine = create_engine(os.getenv('DATABASE_URL'))

    with Session(engine) as session:
        session.add(Log(**input.dict()))
        session.commit()

    return input.json()
