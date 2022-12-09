from tkinter import *
from tkinter.font import Font

class my_list:
    """
    Event planner configuration
    - font
    - frame
    - list box
    """
    
    def __init__(self, event_configuration) -> None:
        self.event_configuration = event_configuration

    def configure(self, root):
        root.title('Calendar Event List')
        root.geometry("600x600")

        # Defining font
        my_font = Font(
            family = "Brush Script MT",
            size = 30, 
            weight = "bold")
        # Create Frame
        my_frame = Frame(root)
        my_frame.pack(pady=10)
        # Creating Listbox
        my_list = Listbox(my_frame,
            font = my_font,
            width =30,
            height = 8,
            bg = "SystemButtonFace",
            bd = 0,
            fg = '#464646',
            highlightthickness = 0,
            selectbackground = "#a6a6a6",
            activestyle="none"
            )
        my_list.pack(side=LEFT, fill = BOTH)

        # CREATE scroll bar
        my_scrollbar = Scrollbar(my_frame)
        my_scrollbar.pack(side=RIGHT, fill=BOTH)
        # add scrollbar
        my_list.config(yscrollcommand=my_scrollbar.set)
        my_scrollbar.config(command=my_list.yview)


        #create an entry box to add items 
        my_entry = Entry(root, font=("Helvetica", 24), width=26)
        my_entry.pack(pady=20)

        #create a button frame
        button_frame =Frame(root)
        button_frame.pack(pady=20)
        
