import os

class SafetyConfig:
    def __init__(self, max_comments_per_hour: int, max_likes_per_hour: int, banned_keywords: list[str]):
        self.max_comments_per_hour = max_comments_per_hour
        self.max_likes_per_hour = max_likes_per_hour
        self.banned_keywords = [k.strip().lower() for k in banned_keywords if k]

    @classmethod
    def from_env(cls):
        max_c = int(os.getenv("MAX_COMMENTS_PER_HOUR", "10"))
        max_l = int(os.getenv("MAX_LIKES_PER_HOUR", "0"))
        banned = os.getenv("BANNED_KEYWORDS", "free,giveaway,follow4follow").split(",")
        return cls(max_c, max_l, banned)

    def is_banned(self, text: str) -> bool:
        t = (text or "").lower()
        return any(k in t for k in self.banned_keywords)
