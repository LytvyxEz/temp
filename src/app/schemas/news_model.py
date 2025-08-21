from pydantic import BaseModel, field_validator, Field

from datetime import datetime, timedelta, timezone
from typing import Optional


class NewsModel(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=25)
    content: str = Field(min_length=10, max_length=500)
    photo_url: Optional[str] = None
    created_at: datetime

    
class NewsSearchFilters(BaseModel):
    created_at: Optional[datetime] = None
    content: Optional[str] = None
    
    
    @field_validator('created_at', mode='before')
    @classmethod
    def validate_created_at(self, v):
        if v and v < datetime.now(timezone.utc) - timedelta(days=60):
            raise ValueError("U can't search news older than 60 days")   
        return v
    
        
class NewsSearch(BaseModel):
    query: str = Field(min_length=5, max_length=25)
    filters: Optional[NewsSearchFilters] = None
    
    
