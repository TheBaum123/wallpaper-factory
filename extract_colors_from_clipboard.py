import re
import pprint
import pyperclip

hex_color_regex = "#[a-fA-F0-9]{6,8}"

text = pyperclip.paste()

colors_found = re.findall(hex_color_regex, text)

colors_found = list(dict.fromkeys(colors_found))

pprint.pprint(colors_found)
