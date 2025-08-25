import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(eq=False, kw_only=True)
class News:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    lead: str
    photo_url: str
    content: str
    is_published: bool
    slug: str
    created_at: datetime

    def __eq__(self, other):
        return isinstance(other, News) and self.id == other.id
