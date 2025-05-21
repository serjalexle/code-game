from datetime import datetime, timezone
from typing import Literal


from beanie import Document
from pydantic import Field

from bson import ObjectId


class User(Document):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    login: str
    bitrix_id: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    password: str
    role: Literal["root", "manager"]

    class Settings:
        name = "users"
        indexes = ["login", "_id", "bitrix_id", "role"]

    def to_dict(self, exclude_password: bool = True) -> dict:
        """
        Method that converts the object to a dictionary and excludes the password if necessary.
        """
        user_dict = self.model_dump()
        if exclude_password:
            user_dict.pop("password", None)
        return user_dict
