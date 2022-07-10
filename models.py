from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date


Base = declarative_base()

class Log(Base):
    __tablename__ = 'log'

    id = Column(Integer, primary_key=True)
    request_id = Column(Integer)
    message = Column(String)
    request_date = Column(Date)

    def __repr__(self):
        return f'[Log {self.id}] request: {self.request_id}'
