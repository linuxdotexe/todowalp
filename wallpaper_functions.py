from crud_functions import read_tasks

import subprocess

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

  subprocess.run([
    'convert',
    './assets/base_image.png',
    '-background', 'none',
    '-fill', '#cdd6f4',
    '-font', './assets/fonts/JetBrainsMono.ttf',
    '-pointsize', '60',
    '-gravity', 'west',
    'label:{}'.format(wallpaper_text),
    '-gravity', 'center',
    '-compose', 'over',
    '-composite', './assets/todowalp.png',
  ])

def set_wallpaper():
  # Set wallpaper
  subprocess.run("feh --bg-scale ./assets/todowalp.png", shell=True)

  print("Wallpaper set")

create_wallpaper()
set_wallpaper()