from pydantic import ResponseModel


class NewsModel(ResponseModel):
    id: int
    lead: str
    content: str
    photo_url: str
