import toga
from toga.style import Pack
from toga.style.pack import COLUMN

def create_border(object, border_color="black", inner_color="#e2985f", padding=(13, 13, 0)) -> toga.Box:
    out_box = toga.Box(style=Pack(direction=COLUMN, padding=padding, background_color=border_color))
    in_box = toga.Box(style=Pack(direction=COLUMN, background_color=inner_color, padding=(2, 2, 2)))
    in_box.add(object)
    out_box.add(in_box)
    return out_box