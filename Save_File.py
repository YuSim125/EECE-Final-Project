from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.title('Calendar Event List')
root.geometry("600x600")

class Save_File:
    
    """ 
    Saving the file of the planner as a .gat file
    so you can open it again the next time the user
    opens up the application.

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

        # create menu
        self.my_menu = Menu(root)
        root.config(menu=self.my_menu)     

        #add items to the menu
        self.file_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="File", menu=self.file_menu)
        # Add dropdown items
        self.file_menu.add_command(label="Save List", command=self.save_list)
 
    # function
    def save_list(self):
            """
            saves the file of the current list to 
            the files of the user's computer
            """
            file_name = filedialog.asksaveasfilename(
            initialdir="C:/gui/data",
            title="Save File",
            filetypes=(
                ("Dat Files", "*.dat"), 
                ("All Files", "*.*"))
            )
            if file_name:
                if file_name.endswith(".dat"):
                    pass
                else:
                    file_name = f'{file_name}.dat'
            # delete crossed items before saving
            count = 0
            while count < self.my_list.size():
                if self.my_list.itemcget(count, "fg") == "#dedede":
                    self.my_list.delete(self.my_list.index(count))
                else:
                    count += 1
            # grab all the stuff from list
            stuff = self.my_list.get(0,END)
            # OPen the file
            output_file = open(file_name, 'wb')

            # Actually add teh stuff to teh file
            pickle.dump(stuff, output_file)

e = Save_File(root)
root.mainloop()