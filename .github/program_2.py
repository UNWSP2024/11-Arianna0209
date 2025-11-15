# Title: Address GUI
# Author: Arianna Endres
# Date: 11/14/2025

# This program displays a window containing my name and address when a "Show Info" button
# is clicked. It also has a "Quit" button which exits the GUI.

import tkinter
import tkinter.messagebox

class GUI_address:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Add a Button widgets with the text 'Show Info' and 'Quit'.
        self.info_button = tkinter.Button(self.main_window, text = 'Show Info',
                                          command = self.open_info_box)

        self.quit_button = tkinter.Button(self.main_window, text = 'Quit',
                                          command = self.main_window.destroy)

        # Pack the Buttons
        self.info_button.pack()
        self.quit_button.pack()

        # Enter main loop.
        tkinter.mainloop()

    def open_info_box(self):
        # Open info dialogue box
        tkinter.messagebox.showinfo('Information',
                                    'Arianna Endres'
                                    '\n1234 Anywhere Street'
                                    '\nRandomville, Minnesota, 55123')

if __name__ == '__main__':
    address_GUI = GUI_address()
