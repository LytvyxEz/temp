from fastapi import APIRouter

from ...schemas import FiltersModel, SearchModel, ProductModel

search_router = APIRouter()


@search_router.get('/search')
async def search():
    return ...