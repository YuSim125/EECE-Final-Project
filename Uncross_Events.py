from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('Calendar Event List')
root.geometry("600x600")

class Uncross_Events:
    
    """ 
    Uncross any events that have been crossed
    because the user may want to plan that
    reminder again.

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

        self.uncross_button = Button(self.button_frame, text="Uncross Event", command=self.uncross_item)
        self.uncross_button.grid(row=0, column=3, padx = 20)
       
    #functions
    def uncross_item(self):
        #cross off item
        self.my_list.itemconfig(
            self.my_list.curselection(),
            fg="#464646")
        #get rid of slection bar
        self.my_list.selection_clear(0, END)

e = Uncross_Events(root)
root.mainloop()