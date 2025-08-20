from fastapi import APIRouter
from src.app.schemas.news_model import NewsModel


router = APIRouter()


@router.get("/news", response_model=NewsModel)
async def news(data: dict = None):
    return {'data': data or []}
