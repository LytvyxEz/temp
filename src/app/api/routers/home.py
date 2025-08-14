from fastapi import APIRouter
from app.schemas.news_model import NewsModel


router = APIRouter()

@router.get("/news", response_model=NewsModel)
async def news(data: dict = None):
    return {'id': 1, 'lead': 'Sample lead', 'content': 'Sample content', 'photo_url': 'http://example.com/photo.jpg'}