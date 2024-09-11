import json
import os
import logging
from pydantic import ValidationError
from fastapi import HTTPException
from models.issue import Issue, UpdateIssue
from logging_config import setup_logging

current_dir = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(current_dir, "issues_data.json")

setup_logging()


def srv_get_issues():
    # Should change this to connect to the Database
    try:
        with open(FILE_PATH, "r") as f:
            issues_data = json.load(f)
    except json.JSONDecodeError as er:
        logging.error(er)
        issues_data = []

    return issues_data


def srv_create_issue(issue):
    issues = srv_get_issues()
    issue["id"] = len(issues) + 1
    try:
        val = Issue(**issue)
    except ValidationError as er:
        logging.error(er)
        raise HTTPException(status_code=400, detail=str(er))

    logging.info(f"Creating issue: {val.model_dump()}")
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
                logging.error(er)
                raise HTTPException(status_code=400, detail=str(er))
            break
    else:
        logging.warning(f"Issue with id {issue_id} not found")
        raise HTTPException(status_code=404, detail="Issue not found")

    logging.info(f"Updating issue: {issue}")

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
        logging.error(f"Issue with id {issue_id} not found")
        raise HTTPException(status_code=404, detail="Issue not found")

    logging.info(f"Deleting issue with id {issue_id}")

    # Should change this to connect to the Database
    with open(FILE_PATH, "w") as f:
        json.dump(issues, f, indent=4)

    return {"message": "Issue deleted"}
