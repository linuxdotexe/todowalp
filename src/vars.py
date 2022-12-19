# Author: Venkata Naga Sai Nivas Mangu
# Contact: sainonbeat99@gmail.com

# SOLVING THE PATH PROBLEM
from config.definitions import ROOT_DIR
import os

BASE_IMAGE_PATH = os.path.join(ROOT_DIR, "assets", "base_image.png")
FONT_PATH = os.path.join(ROOT_DIR, "assets", "fonts", "JetBrainsMono.ttf")

# Customizable factors of the convert command
# All variables will be explained in docs
variables_dict = {
  "base_image": BASE_IMAGE_PATH,
  "background": "none",
  "fill": "#cdd6f4",
  "font": FONT_PATH,
  "pointsize": "35",
  "empty_text": "Custom empty wallpaper text."
}
