# Create a service to get user info
import threading
from asyncio.windows_events import NULL

from fastapi import Request


class GetUserInfoService:
    __singleton_lock = threading.Lock()
    __singleton_instance = None

    @classmethod
    def instance(cls):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls()
        return cls.__singleton_instance
    
    def get_info_by_username(self, username: str, request: Request) -> dict:
        return {
            "username": username,
            "query_params":request.query_params
            }
