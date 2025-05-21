from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

scheduler = AsyncIOScheduler()


def start_scheduler():
    # scheduler.add_job(
    #     decryption_cleanup_job,
    #     trigger=IntervalTrigger(minutes=1),
    #     id="decryption_cleanup_job",
    #     name="Clean up old decryption requests",
    #     replace_existing=True,
    #     max_instances=1,
    #     coalesce=True,    # 🔁 miss job if previous not completed
    # )
    scheduler.start()
