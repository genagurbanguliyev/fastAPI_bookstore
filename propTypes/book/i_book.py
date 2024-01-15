from typing import Optional
from pydantic import BaseModel, Field


class IBook(BaseModel):
    id: Optional[int] = Field(default=None, title="id is not needed")
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=0, le=5),
    published_date: int = Field(gt=2023, lt=2031)

    class Config:
        json_schema_extra = {
            'example': {
                'title': "Python in a Nutshell",
                'author': "gena",
                'description': "Python in a Nutshell",
                'rating': 5,
                'published_date': '2024'
            }
        }
