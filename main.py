# Author: Venkata Naga Sai Nivas Mangu
# Contact: sainonbeat99@gmail.com

# Import SQLite
import sqlite3

# Import sys for taking command line arguments
import sys

# Import functions for DB operations
from functions import insert_tasks, read_tasks, update_tasks, delete_task, help

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

# Define flag for insert_tasks
if len(sys.argv) > 1:
  if sys.argv[1] == "-i" or sys.argv[1] == "i" or sys.argv[1] == "--insert":
    try:
      insert_tasks(sys.argv[2])
    except IndexError:
      print("Not enough arguments. Enter the name of the task.")

  # Define flag for delete_task
  elif sys.argv[1] == "-d" or sys.argv[1] == "d" or sys.argv[1] == "--delete":
    try:
      delete_task(sys.argv[2])
    except IndexError:
      print("Not enough arguments. Enter the name of the task.")

  # Define flag for update_tasks
  elif sys.argv[1] == "-u" or sys.argv[1] == "u" or sys.argv[1] == "--update":
    update_tasks()

  # Define flag for help
  elif sys.argv[1] == "-h" or sys.argv[1] == "h" or sys.argv[1] == "--help":
    help()
else:
  read_tasks()