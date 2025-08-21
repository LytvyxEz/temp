from fastapi import APIRouter

from src.app.schemas.news_model import NewsModel, NewsSearch


news_router = APIRouter()


@news_router.get("/news", response_model=NewsModel)
async def news_get(data: dict = None):
    return {'data': data or []}


@news_router.post('/news')
async def news_post():
    return ...


@news_router.get('/news_search')
async def news_search_get():
    return ...


@news_router.post('/news_search')
async def news_search_post():
    return ...