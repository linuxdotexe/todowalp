# Author: Venkata Naga Sai Nivas Mangu
# Contact: sainonbeat99@gmail.com

# Import SQLite
import sqlite3

# Create connection to the database
connection = sqlite3.connect("./db/todo.db")
cursor = connection.cursor()

# Function to read all the tasks in the table
def read_tasks():
  query="SELECT * FROM todo ORDER BY status ASC"
  cursor.execute(query)   
  rows=cursor.fetchall()
  return rows

# Function to store insert data into the DB
def insert_tasks(task_name):
  try:
    cursor.execute("INSERT INTO todo(task_name, status) VALUES(?, ?)", (task_name, 0,))
  except sqlite3.IntegrityError:
    print("Task already exists. Insertion ignored.")
  connection.commit()

# Function to delete a task
def delete_task(task_name):
  cursor.execute("DELETE FROM todo WHERE task_name IS ?", (task_name,))
  connection.commit()

# Bulk delete all completed tasks
def delete_all_finished_tasks():
  cursor.execute("DELETE FROM todo WHERE status is 1")
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

def help():
  print("""Usage: todowalp [options [parameters]]

  Options:
      -h (or) --help (or) h, Print this menu
      Example: todowalp -h
      
      -i (or) --insert (or) i, Insert a task into the table
      Example: todowalp -i taskname
      
      -d (or) --delete (or) d, Delete a task from the table
      Example: todowalp -d taskname

      -u (or) --update (or) u, Update a task from the table
      Example: todowalp -u

      To get all the tasks in the table, 
      enter the command with no parameters.
  """)
