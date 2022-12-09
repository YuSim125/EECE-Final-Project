from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.title('Calendar Event List')
root.geometry("600x600")

class Open_File:
    
    """ 
    Open the file of any file that the user saved
    in their computer the last time they opened the 
    planner application.
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

        self.file_menu.add_command(label="Open List", command=self.open_list)
    
    #functions       
    def open_list(self):
            """
            opens a saved file from the user's
            computer of any past planners.
            """
            file_name = filedialog.askopenfilename(
            initialdir="C:/gui/data",
            title="Save File",
            filetypes=(
                ("Dat Files", "*.dat"), 
                ("All Files", "*.*"))
            ) 
            if file_name:
            #delete currently open list
                self.my_list.delete(0, END)
            #open the file:
                input_file = open(file_name, 'rb')

            #load the data
            stuff = pickle.load(input_file)

            #output the stuff
            for item in stuff:
                self.my_list.insert(END, item)

e = Open_File(root)
root.mainloop()