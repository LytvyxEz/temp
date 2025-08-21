from fastapi import FastAPI

from .routers import router, search_router, news_router


app = FastAPI()
app.include_router(router)
app.include_router(search_router)
app.include_router(news_router)
