from typing import Optional

from fastapi import Request
from services.instagram.get_user_info import GetUserInfoService

UserService = GetUserInfoService.instance()

async def get_info_by_username(username: str , request: Request):
    try:
        result = UserService.get_info_by_username(username=username, request=request)
        return result
    except Exception as e:
        return {
            "error": str(e)
        }

