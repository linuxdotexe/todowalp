# Author: Venkata Naga Sai Nivas Mangu
# Contact: sainonbeat99@gmail.com

# Import SQLite
import sqlite3

# Import functions for DB operations
from functions import insert_tasks, read_tasks, update_tasks, delete_task

# Create connection to the database
connection = sqlite3.connect("./db/todo.db")
cursor = connection.cursor()

# Create a table in the database
create_table = """
CREATE TABLE IF NOT EXISTS todo(
  task_name TEXT UNIQUE,
  status BOOLEAN
)"""
cursor.execute(create_table)

read_tasks()