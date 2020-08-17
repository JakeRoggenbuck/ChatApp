import os.path
import sqlite3
from datetime import datetime


class DataBase:
    def __init__(self):
        self.db_name = "database.db"

    def check_file(self):
        # Check for db
        return os.path.isfile(self.db_name)

    def setup_db(self):
        # If file doesn't exist make table
        if not self.check_file():
            self.connect_db()
            self.create_table()

    def connect_db(self):
        # Connect to database
        return sqlite3.connect(self.db_name)

    def create_table(self):
        sql_command = """
            CREATE TABLE message (
            message_number INTEGER PRIMARY KEY,
            content VARCHAR(2000),
            author VARCHAR(50),
            time TIME);"""
        self.write_db(sql_command)

    def write_db(self, command, *value):
        # Write raw command
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(command, *value)
        connection.commit()

    def write(self, content, author, time):
        # Write data as message
        sql_command = """INSERT INTO message
        (message_number, content, author, time)
        VALUES (NULL, ?, ?, ?);"""
        self.write_db(sql_command, (content, author, time))

    def read_db(self, command, *value):
        # Read raw command
        connection = self.connect_db()
        cursor = connection.cursor()
        cursor.execute(command, *value)
        result = cursor.fetchall()
        return result

    def read_all(self):
        # Read all messages
        data = "SELECT * FROM message"
        return self.read_db(data)
