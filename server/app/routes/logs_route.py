from fastapi import APIRouter, Query

from app.models.history_log import HistoryLog

logs_router = APIRouter(prefix="/api/logs", tags=["Logs"])


@logs_router.get("/")
async def get_logs_route(
    page: int = Query(1),
    count: int = Query(10),
):
    """
    Get paginated history logs.
    """

    logs = await HistoryLog.find().sort("-created_at").to_list()
    total_count = await HistoryLog.count()
    start_index = (page - 1) * count
    end_index = start_index + count
    paginated_logs = logs[start_index:end_index]

    return {
        "status": "success",
        "result": {
            "data": paginated_logs,
            "meta": {
                "page": page,
                "count": count,
                "total": total_count,
            },
        },
    }
