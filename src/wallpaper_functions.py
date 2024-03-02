# Author: Venkata Naga Sai Nivas Mangu
# Contact: sainonbeat99@gmail.com

# SOLVING THE PATH PROBLEM
from config.definitions import ROOT_DIR
import os

TODOWALP_PATH = os.path.join(ROOT_DIR, "assets", "todowalp.png")

# Importing functions and vars
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
    wallpaper_text = variables_dict["empty_text"]
  else:
    for key, value in task_list.items():
      if value == 0:
        wallpaper_text += ". " + key + "\\n"
      else:
        wallpaper_text += "x " + key + "\\n"

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
    '-composite', TODOWALP_PATH,
  ])
  set_wallpaper()

def set_wallpaper():
  # Set wallpaper
  current_de = os.environ["DESKTOP_SESSION"]

  if (current_de == "gnome"):
    subprocess.run("gsettings set org.gnome.desktop.background picture-uri-dark {}".format(TODOWALP_PATH), shell=True)
  else:
    subprocess.run("feh --bg-scale {}".format(TODOWALP_PATH), shell=True)

  # TODO: Look into XDG_CURRENT_DESKTOP
