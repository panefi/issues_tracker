from pydantic import BaseModel
from typing import Optional


class Issue(BaseModel, extra="forbid"):
    title: str
    description: str
    status: str


class UpdateIssue(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
