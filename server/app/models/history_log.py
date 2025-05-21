from datetime import datetime, timezone
from typing import List, Optional
from beanie import Document
from pydantic import BaseModel, Field
from bson import ObjectId


class LogStage(BaseModel):
    subtitle: str
    error: Optional[str] = None
    isSuccess: bool


class HistoryLog(Document):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    bitrix_user_id: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    title: str
    isSuccess: bool
    log_stages: List[LogStage] = Field(default_factory=list)

    class Settings:
        name = "history_logs"
        indexes = ["bitrix_user_id", "id", "created_at"]
