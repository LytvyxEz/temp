from pydantic import ResponseModel
from datetime import datetimeField

class NewsModel(ResponseModel):
    id: int
    lead: str
    content: str
    photo_url: str