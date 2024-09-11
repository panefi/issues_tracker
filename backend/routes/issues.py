from fastapi import APIRouter
from services.issues import srv_get_issues, srv_create_issue, srv_update_issue

#create a fastapi app
router = APIRouter()

#add logging to all functionalities
import logging
logging.basicConfig(level=logging.INFO)


@router.get("/issues")
def get_issues():
    issues = srv_get_issues()
    return issues

@router.post("/issue")
def create_issue(issue: dict):
    new_issue = srv_create_issue(issue)
    return new_issue

@router.put("/issue/{issue_id}")
def update_issue(issue_id: int, body: dict):
    updated_issue = srv_update_issue(issue_id, body)
    return updated_issue