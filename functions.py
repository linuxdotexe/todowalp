# Author: Venkata Naga Sai Nivas Mangu
# Contact: sainonbeat99@gmail.com

# Import SQLite
import sqlite3

# Create connection to the database
connection = sqlite3.connect("./db/todo.db")
cursor = connection.cursor()

# Function to read all the tasks in the table
def read_tasks():
  query="SELECT * FROM todo"
  cursor.execute(query)   
  rows=cursor.fetchall()
  print(rows)

# Function to store insert data into the DB
def insert_tasks():
  task_name = input("Enter task name: ")
  try:
    cursor.execute("INSERT INTO todo(task_name, status) VALUES(?, ?)", (task_name, 0,))
  except sqlite3.IntegrityError:
    print("Task already exists. Insertion ignored.")
  connection.commit()

# Function to delete a task
def delete_task():
  task_name = input("Enter the task name that is to be deleted: ")
  cursor.execute("DELETE FROM todo WHERE task_name IS ?", (task_name,))
  connection.commit()

# Function to update task data in the DB
def update_tasks():
  update_option = int(input("""
  What is the update?
  1. Mark a task as completed
  2. Mark a completed task as incomplete
  """))
  
  if update_option == 1:
    task_name = input("Enter the task name that is to be marked complete: ")
    cursor.execute("UPDATE todo SET status = 1 WHERE task_name IS ?", (task_name,))
    connection.commit()

  elif update_option == 2:
    task_name = input("Enter the task name that is to be marked incomplete: ")
    cursor.execute("UPDATE todo SET status = 0 WHERE task_name IS ?", (task_name,))
    connection.commit()
    
  else:
    print("Enter a valid option.")