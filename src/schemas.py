from pydantic import BaseModel
from typing import Optional

class BlogModel(BaseModel):
    title: str
    content: Optional[str] = "my content ..."

class BlogUpdateModel(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
