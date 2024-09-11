import json
import os
from pydantic import ValidationError
from fastapi import HTTPException
from models.issue import Issue, UpdateIssue

current_dir = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(current_dir, "issues_data.json")


def srv_get_issues():
    # Should change this to connect to the Database
    try:
        with open(FILE_PATH, "r") as f:
            issues_data = json.load(f)
    except json.JSONDecodeError:
        issues_data = []

    return issues_data


def srv_create_issue(issue):
    issues = srv_get_issues()
    issue["id"] = len(issues) + 1
    try:
        val = Issue(**issue)
    except ValidationError as er:
        raise HTTPException(status_code=400, detail=str(er))

    # Should change this to connect to the Database
    issues.append(val.model_dump())
    with open(FILE_PATH, "w") as f:
        json.dump(issues, f, indent=4)

    return issue


def srv_update_issue(issue_id, body):
    issues = srv_get_issues()
    for issue in issues:
        if issue["id"] == issue_id:
            try:
                val = UpdateIssue(**body)
                for key, value in val.model_dump().items():
                    if value is not None:
                        issue[key] = value
            except ValidationError as er:
                raise HTTPException(status_code=400, detail=str(er))
            break
    else:
        raise HTTPException(status_code=404, detail="Issue not found")

    # Should change this to connect to the Database
    with open(FILE_PATH, "w") as f:
        json.dump(issues, f, indent=4)

    return issue


def srv_delete_issue(issue_id):
    issues = srv_get_issues()
    for issue in issues:
        if issue["id"] == issue_id:
            issues.remove(issue)
            break
    else:
        raise HTTPException(status_code=404, detail="Issue not found")

    # Should change this to connect to the Database
    with open(FILE_PATH, "w") as f:
        json.dump(issues, f, indent=4)

    return {"message": "Issue deleted"}
