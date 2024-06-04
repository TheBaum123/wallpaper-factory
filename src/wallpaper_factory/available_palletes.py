import json
import os
from PIL import ImageColor


def convert_array(array_hex):
    rgba_colors = []
    for color in array_hex:
        rgba_colors.append(ImageColor.getcolor(color, "RGBA"))
    return rgba_colors


available_palletes = []
f = open(os.path.join(os.path.dirname(__file__), "palletes.json"))
palettes = f.read()
palettes = json.loads(palettes)
palettes = [[scheme, colors] for scheme, colors in palettes.items()]
for arr in palettes:
    available_palletes.append([arr[0], convert_array(arr[1])])
