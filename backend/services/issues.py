import json
import logging
from pydantic import ValidationError
from fastapi import HTTPException
from models.issue import Issue, UpdateIssue
from logging_config import setup_logging
import database.database as database
import database.queries as db_queries


setup_logging()


def srv_get_issues():
    try:
        with database.SQLConnection() as db:
            issues_data = db.execute_query(db_queries.GET_ISSUES_FOR_CUSTOMER_NAME, ("Test Company 1",))
    except Exception as er:
        logging.error(er)
        issues_data = []

    return issues_data


def srv_create_issue(issue):
    try:
        val = Issue(**issue)
    except ValidationError as er:
        logging.error(er)
        raise HTTPException(status_code=400, detail=str(er))

    logging.info(f"Creating issue: {val.model_dump()}")

    with database.SQLConnection() as db:
        db.execute_query(
            db_queries.CREATE_ISSUE,
            (issue["title"], issue["description"], issue["status"], "Test Company 1")
        )

    return issue


def srv_update_issue(issue_id, issue_data):
    try:
        val = UpdateIssue(**issue_data)
    except ValidationError as er:
        logging.error(er)
        raise HTTPException(status_code=400, detail=str(er))

    logging.info(f"Updating issue: {val.model_dump()}")

    updates = []
    params = []

    if "title" in issue_data:
        updates.append("title=%s")
        params.append(issue_data["title"])
    if "description" in issue_data:
        updates.append("description=%s")
        params.append(issue_data["description"])
    if "status" in issue_data:
        updates.append("status=%s")
        params.append(issue_data["status"])

    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update")

    params.append(issue_id)
    query = db_queries.UPDATE_ISSUE.format(updates=", ".join(updates))

    with database.SQLConnection() as db:
        db.execute_query(query, params)

    return {"issue_id": issue_id, **issue_data}


def srv_delete_issue(issue_id):
    logging.info(f"Deleting issue with id {issue_id}")

    try:
        with database.SQLConnection() as db:
            # Check if the issue exists
            existing_issue = db.execute_query("SELECT 1 FROM issues WHERE issue_id=%s", (issue_id,))
            if not existing_issue:
                logging.error(f"Issue with id {issue_id} not found")
                raise HTTPException(status_code=404, detail="Issue not found")

            # Delete the issue
            db.execute_query(db_queries.DELETE_ISSUE, (issue_id,))
            logging.info(f"Issue with id {issue_id} deleted successfully")
    except Exception as er:
        logging.error(f"Database error: {er}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return {"message": "Issue deleted"}
