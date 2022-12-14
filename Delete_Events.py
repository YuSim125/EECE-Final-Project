from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('Calendar Event List')
root.geometry("600x600")

class Delete_Events:
    
    """ 
    Delete button which will delete any 
    added events that were accidently made.

    """
    def __init__(self,root):
        myFrame = Frame(root)
        myFrame.pack()
    # Defining font
        self.my_font = Font(
            family = "Times New Roman",
            size = 20, 
            weight = "bold")
    # Create Frame
        self.my_frame = Frame(root)
        self.my_frame.pack(pady=10)
    # Creating Listbox
        self.my_list = Listbox(self.my_frame,
            font = self.my_font,
            width =30,
            height = 8,
            bg = "SystemButtonFace",
            bd = 0,
            fg = '#464646',
            highlightthickness = 0,
            selectbackground = "#a6a6a6",
            activestyle="none"
            )    
        self.my_list.pack(side=LEFT, fill = BOTH)

    # CREATE scroll bar
        self.my_scrollbar = Scrollbar(self.my_frame)
        self.my_scrollbar.pack(side=RIGHT, fill=BOTH)
    # add scrollbar
        self.my_list.config(yscrollcommand=self.my_scrollbar.set)
        self.my_scrollbar.config(command=self.my_list.yview)


    #create an entry box to add items 
        self.my_entry = Entry(root, font=("Helvetica", 24), width=26)
        self.my_entry.pack(pady=20)

    #create a button frame
        self.button_frame =Frame(root)
        self.button_frame.pack(pady=20)

        self.delete_button = Button(self.button_frame, text="Delete Event", command=self.delete_item)
        self.delete_button.grid(row=0, column=1, padx = 20)

    #functions
    def delete_item(self):
        """
        deleting item that has been marked by the user's 
        cursor and with the press of the button
        the item deletes itself. 
        
        """
        self.my_list.delete(ANCHOR)

e = Delete_Events(root)
root.mainloop()