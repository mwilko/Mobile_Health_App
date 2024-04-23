from toga import Window, Box, Label

class PopupWindow:
    def show_message(message):
        # Create a new window
        popup = Window(title="Message")

        # Create a box to hold the contents of the window
        box = Box()

        # Add widgets to the box
        label = Label(message)
        box.add(label)

        # Add the box to the window
        popup.content = box

        # Show the window
        popup.show()