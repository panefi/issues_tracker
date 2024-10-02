"""Database Queries"""

GET_ISSUES_FOR_CUSTOMER_NAME = """
SELECT i.issue_id, i.title, i.description, i.status, i.created_at, c.name AS customer_name
FROM issues i
JOIN customers c ON i.customer_id = c.customer_id
WHERE c.name = %s;
"""

CREATE_ISSUE = """
INSERT INTO issues (title, description, status, customer_id)
VALUES (%s, %s, %s, (SELECT customer_id FROM customers WHERE name = %s));
"""

UPDATE_ISSUE = """
UPDATE issues
SET {updates}
WHERE issue_id=%s ;
"""

DELETE_ISSUE = "DELETE FROM issues WHERE issue_id=%s"
