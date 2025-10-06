from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

_scheduler = None

def _heartbeat():
    print(f"[scheduler] heartbeat {datetime.utcnow().isoformat()}Z")

def scheduler_start():
    global _scheduler
    if _scheduler:
        return _scheduler
    _scheduler = BackgroundScheduler(timezone="UTC")
    _scheduler.add_job(_heartbeat, "interval", minutes=5, id="heartbeat")
    _scheduler.start()
    return _scheduler
