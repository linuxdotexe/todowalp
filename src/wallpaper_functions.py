# Author: Venkata Naga Sai Nivas Mangu
# Contact: sainonbeat99@gmail.com

from src.crud_functions import read_tasks
from src.vars import variables_dict

# Import subprocess to run shell commands (imagemagick)
import subprocess

# Function to create a wallpaper
def create_wallpaper():
  # Get todo
  task_list = read_tasks()
  task_list = dict(task_list)
  # Put todo on image
  wallpaper_text = ""
  if len(task_list) == 0:
    wallpaper_text = "No tasks listed."
  else:
    for key, value in task_list.items():
      if value == 0:
        wallpaper_text += "[ ] " + key + "\\n"
      else:
        wallpaper_text += "[X] " + key + "\\n"

  # explanation p1: https://www.reddit.com/r/learnpython/comments/x1lte4/error_with_ossystem/
  # explanation p2: https://stackoverflow.com/questions/73550468/align-text-to-left-with-imagemagick
  subprocess.run([
    'convert',
    variables_dict["base_image"],
    '-background', variables_dict["background"],
    '-fill', variables_dict["fill"], # var
    '-font', variables_dict["font"], # var
    '-pointsize', variables_dict["pointsize"], # var
    '-gravity', 'west',
    'label:{}'.format(wallpaper_text),
    '-gravity', 'center',
    '-compose', 'over',
    '-composite', './assets/todowalp.png',
  ])
  set_wallpaper()

def set_wallpaper():
  # Set wallpaper
  subprocess.run("feh --bg-scale ./assets/todowalp.png", shell=True)