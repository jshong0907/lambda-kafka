from lib2to3.pytree import Base
from datetime import date

from pydantic import BaseModel
from pydantic import validator


class InputSchema(BaseModel):
    request_id: int
    message: str = ''
    request_date: date

    @validator('request_date')
    def validate_request_date(cls, v):
        """요청일 검증
        
        요청일은 2022년 7월이어야한다.
        """
        if v.year != 2022 or v.month != 7:
            raise ValueError('Request date must be July 2022')
        return v
