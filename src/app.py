from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.rules.filters import SafetyConfig
from src.scheduler import scheduler_start

app = FastAPI(title="Instagram Engagement Bot (Compliant)")

class EnqueueCommentJob(BaseModel):
    media_id: str
    text: str

@app.on_event("startup")
async def on_startup():
    scheduler_start()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/jobs/comment")
def enqueue_comment(job: EnqueueCommentJob):
    sc = SafetyConfig.from_env()
    if sc.is_banned(job.text):
        raise HTTPException(status_code=400, detail="Text contains banned keywords")
    # Normally enqueue; here we just validate:
    return {"queued": True, "media_id": job.media_id, "text": job.text}
