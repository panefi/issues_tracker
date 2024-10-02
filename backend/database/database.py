import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


class SQLConnection:
    def __init__(self):
        """Connects to the database"""
        self.mydb = None

    def __enter__(self):
        """Establish the database connection"""
        self.mydb = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )
        self.mydb.start_transaction()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the database connection"""
        if exc_type is None:
            self.mydb.commit()
        else:
            self.mydb.rollback()
        if self.mydb:
            self.mydb.close()

    def execute_query(self, query, params=None):
        """Executes a query and returns the result"""
        mycursor = self.mydb.cursor(dictionary=True)
        mycursor.execute(query, params)
        return mycursor.fetchall()
