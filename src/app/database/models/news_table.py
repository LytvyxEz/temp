import datetime

from sqlalchemy import Table, Column, String, UUID, Boolean, Text, DateTime

from src.app.domain import News
from src.app.database.orm_registry import mapping_registry


news_table = Table(
    'news',
    mapping_registry.metadata,
    Column('id', UUID(as_uuid=True), primary_key=True),
    Column('lead', String(75), unique=True),
    Column('photo_url', String(255)),
    Column('content', Text),
    Column('is_published', Boolean, default=False),
    Column('slug', Text, unique=True),
    Column('created_at', DateTime, default=datetime.datetime.utcnow)
)


def map_news_table() -> None:
    mapping_registry.map_imperatively(
        News,
        news_table
    )
