from pydantic import BaseModel
from typing import List, Optional
from app.dto.common import metaDTO


class LogStageDTO(BaseModel):
    subtitle: str
    error: Optional[str] = None
    isSuccess: bool


class HistoryLogEntryDTO(BaseModel):
    id: str
    bitrix_user_id: str
    title: str
    isSuccess: bool
    log_stages: List[LogStageDTO]


class HistoryLogsResultDTO(BaseModel):
    data: List[HistoryLogEntryDTO]
    meta: metaDTO


class AppHistoryLogResponseDTO(BaseModel):
    status: str
    result: HistoryLogsResultDTO
    message: Optional[str] = ""



class CreateLogStageDTO(BaseModel):
    subtitle: str
    error: Optional[str] = None
    isSuccess: bool


class CreateHistoryLogDTO(BaseModel):
    bitrix_user_id: str
    title: str
    isSuccess: bool
    log_stages: List[CreateLogStageDTO]
