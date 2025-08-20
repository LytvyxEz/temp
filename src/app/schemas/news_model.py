from pydantic import BaseModel


class NewsModel(BaseModel):
    id: int
    lead: str
    content: str
    photo_url: str
    created_at: str
    
    