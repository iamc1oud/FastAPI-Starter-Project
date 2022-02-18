from typing import Optional

from controllers.instagram import user_info
from fastapi import APIRouter, Request

router = APIRouter()

# Define routes
router.get("/profile/")(user_info.get_info_by_username)
