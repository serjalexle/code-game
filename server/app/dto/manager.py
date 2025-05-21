from pydantic import BaseModel
from typing import List


class ManagerCreateDTO(BaseModel):
    bitrix_user_id: str
    department_ids: List[str]

class ManagerEditDTO(BaseModel):
    bitrix_user_id: str = None
    department_ids: List[str] = None