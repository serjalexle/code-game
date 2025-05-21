from datetime import datetime, timezone
from typing import Literal


from beanie import Document
from pydantic import Field

from bson import ObjectId


class Manager(Document):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    bitrix_user_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    created_by: str = Field(default="system")
    department_ids: list[str] = Field(default_factory=list)

    class Settings:
        name = "managers"
        indexes = ["bitrix_user_id", "id", "created_by", "department_ids"]

    def to_dict(self, exclude_password: bool = True) -> dict:
        """
        Method that converts the object to a dictionary and excludes the password if necessary.
        """
        user_dict = self.model_dump()
        return user_dict
