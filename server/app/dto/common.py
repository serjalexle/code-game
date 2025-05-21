from pydantic import BaseModel


class metaDTO(BaseModel):
    total: int
    page: int
    count: int
