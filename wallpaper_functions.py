from crud_functions import read_tasks

import os

# Function to create a wallpaper
def create_wallpaper():
  # Get todo
  task_list = read_tasks()
  task_list = dict(task_list)
  # Put todo on image
  wallpaper_text = ""
  for key, value in task_list.items():
    if value == 0:
      wallpaper_text += "[ ] " + key + "\\n"
    else:
      wallpaper_text += "[X] " + key + "\\n"

  create_wallpaper_command = "convert ./assets/base_image.png -gravity Center -font ./assets/fonts/JetBrainsMono.ttf -pointsize 30 -fill #cdd6f4 -annotate 0 '{}' ./assets/todowalp.png".format(wallpaper_text)

  print(create_wallpaper_command)
  # os.system(create_wallpaper_command)

def set_wallpaper():
  # Set wallpaper

  print("Wallpaper set")

create_wallpaper()