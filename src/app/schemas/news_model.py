from pydantic import BaseModel, field_validator
from typing import Optional, Union


class NewsModel(BaseModel):
    id: int
    lead: str
    content: str
    photo_url: str
    created_at: str
    
    
class NewsSearchFilters(BaseModel):
    title: str
    created_at: Optional[str] = None
    content: Optional[str] = None
    
        
class NewsSearch(BaseModel):
    query: str
    filters: Optional[NewsSearchFilters] = None
    