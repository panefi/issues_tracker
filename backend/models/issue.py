from pydantic import BaseModel
from typing import Optional

class Issue(BaseModel):
    title: str
    description: str
    status: str
    id: int


class UpdateIssue(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]