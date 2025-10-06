from abc import ABC, abstractmethod
from typing import Any, Dict

class SocialClient(ABC):
    @abstractmethod
    async def create_comment(self, media_id: str, text: str) -> Dict[str, Any]:
        ...

    @abstractmethod
    async def get_recent_mentions(self) -> Dict[str, Any]:
        ...

    @abstractmethod
    async def get_own_media(self) -> Dict[str, Any]:
        ...
