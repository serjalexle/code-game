from app.dto.history_logs import (
    AppHistoryLogResponseDTO,
    CreateHistoryLogDTO,
    CreateLogStageDTO,
)
from app.models.history_log import HistoryLog


class HistoryLogService:
    @staticmethod
    async def create_log(data: CreateHistoryLogDTO) -> HistoryLog:
        log = HistoryLog(
            bitrix_user_id=data.bitrix_user_id,
            title=data.title,
            isSuccess=data.isSuccess,
            log_stages=[
                CreateLogStageDTO(**stage.model_dump()) for stage in data.log_stages
            ],
        )
        await log.insert()
        return log

    @staticmethod
    async def get_logs(
        bitrix_user_id: str, page: int = 1, count: int = 10
    ) -> AppHistoryLogResponseDTO:
        skip = (page - 1) * count
        logs_query = HistoryLog.find(HistoryLog.bitrix_user_id == bitrix_user_id)
        total = await logs_query.count()
        logs = await logs_query.skip(skip).limit(count).to_list()
        return {
            "status": "success",
            "result": {
                "data": logs,
                "meta": {
                    "total": total,
                    "page": page,
                    "count": count,
                },
            },
        }
