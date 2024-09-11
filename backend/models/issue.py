from pydantic import BaseModel
from typing import Optional

class Issue(BaseModel):
    title: str
    description: str
    status: str
    id: int


class UpdateIssue(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None