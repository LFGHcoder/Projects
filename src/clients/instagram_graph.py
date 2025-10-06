import os
import httpx
from typing import Any, Dict
from src.clients.base import SocialClient

BASE = "https://graph.facebook.com/v20.0"

class InstagramGraphClient(SocialClient):
    def __init__(self):
        self.access_token = os.getenv("IG_GRAPH_ACCESS_TOKEN", "")
        self.account_id = os.getenv("IG_ACCOUNT_ID", "")
        if not self.access_token or not self.account_id:
            raise ValueError("Missing IG_GRAPH_ACCESS_TOKEN or IG_ACCOUNT_ID")

    async def create_comment(self, media_id: str, text: str) -> Dict[str, Any]:
        url = f"{BASE}/{media_id}/comments"
        async with httpx.AsyncClient(timeout=20) as client:
            r = await client.post(url, data={"message": text, "access_token": self.access_token})
            r.raise_for_status()
            return r.json()

    async def get_recent_mentions(self) -> Dict[str, Any]:
        url = f"{BASE}/{self.account_id}/mentioned_media?access_token={self.access_token}"
        async with httpx.AsyncClient(timeout=20) as client:
            r = await client.get(url)
            r.raise_for_status()
            return r.json()

    async def get_own_media(self) -> Dict[str, Any]:
        url = f"{BASE}/{self.account_id}/media?access_token={self.access_token}"
        async with httpx.AsyncClient(timeout=20) as client:
            r = await client.get(url)
            r.raise_for_status()
            return r.json()
