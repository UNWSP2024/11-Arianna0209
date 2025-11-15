# Title: Favorite Verse
# Author: Arianna Endres
# Date: 11/14/2025

# This program displays a window containing my favorite verse.

import tkinter

class GUI_favorite_verse:
    def __init__(self):
        # Create the window widget.
        self.window = tkinter.Tk()

        # Add a title.
        self.window.title('My Favorite Verse')

        # Add text.
        self.label = tkinter.Label(self.window, text='For God so loved the world, '
                                                     '\nthat he gave his only begotten Son, '
                                                     '\nthat whosoever believeth in him '
                                                     '\nshould not perish, but have everlasting life.')

        # Call Label widget's pack method.
        self.label.pack()

        # Enter main loop.
        tkinter.mainloop()

if __name__ == '__main__':
    favorite_verse_GUI = GUI_favorite_verse()
