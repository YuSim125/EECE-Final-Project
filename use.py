from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle
from my_list import my_list
root = Tk()
root.title('Calendar Event List')
root.geometry("600x600")
class Event_Planner:
    
    """ 
    Event planner where you can add and delete and 
    have other options to work on your
    events. 

    """
    def __init__(self,root):
        myFrame = Frame(root)
        myFrame.pack()
    # Defining font
        self.my_font = Font(
            family = "Times New Roman",
            size = 30, 
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
    # # create dummy list
    # stuff = ["I love Ling", "Rule the world"]
    # # add dummy list to listbox
    # for item in stuff:
    #     my_list.insert(END, item)

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
        self.file_menu.add_command(label="Open List", command=self.open_list)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Clear List", command=self.clear_list)


        self.add_button = Button(self.button_frame, text="Add Event", command=self.add_item)
        self.delete_button = Button(self.button_frame, text="Delete Event", command=self.delete_item)
        self.cross_off_button = Button(self.button_frame, text="Cross off Event", command=self.cross_off_item)
        self.uncross_button = Button(self.button_frame, text="Uncross Event", command=self.uncross_item)
        self.delete_crossed_button = Button(self.button_frame, text="Delete Crossed Event", command=self.delete_crossed_item)

        self.add_button.grid(row=0, column=0)        
        self.delete_button.grid(row=0, column=1, padx = 20)
        self.cross_off_button.grid(row=0, column=2)
        self.uncross_button.grid(row=0, column=3, padx = 20)
        self.delete_crossed_button.grid(row=0, column=4)


    
    #functions
    def delete_item(self):
        self.my_list.delete(ANCHOR)

    def add_item(self):
        
        self.my_list.insert(END, self.my_entry.get())
        self.my_entry.delete(0, END)

    def cross_off_item(self):
        #cross off item
        self.my_list.itemconfig(
            self.my_list.curselection(),
            fg="#dedede")
        #get rid of slection bar
        self.my_list.selection_clear(0, END)

    def uncross_item(self):
        #cross off item
        self.my_list.itemconfig(
            self.my_list.curselection(),
            fg="#464646")
        #get rid of slection bar
        self.my_list.selection_clear(0, END)

    def delete_crossed_item(self):
        self.count = 0
        while self.count < self.my_list.size():
            if self.my_list.itemcget(self.count, "fg") == "#dedede":
                self.my_list.delete(self.my_list.index(self.count))
            else:
                self.count += 1


    def save_list(self):
        self.file_name = filedialog.asksaveasfilename(
            initialdir="C:/gui/data",
            title="Save File",
            filetypes=(
                ("Dat Files", "*.dat"), 
                ("All Files", "*.*"))
            )
        if self.file_name:
            if self.file_name.endswith(".dat"):
                pass
            else:
                self.file_name = f'{self.file_name}.dat'
            # delete crossed items before saving
            self.count = 0
            while self.count < self.my_list.size():
                if self.my_list.itemcget(self.count, "fg") == "#dedede":
                    self.my_list.delete(self.my_list.index(self.count))
                else:
                    self.count += 1
            # grab all the stuff from list
            self.stuff = my_list.get(0,END)
            # OPen the file
            self.output_file = open(self.file_name, 'wb')

            # Actually add teh stuff to teh file
            self.pickle.dump(self.stuff, self.output_file)


                
    def open_list(self):
        self.file_name = filedialog.askopenfilename(
            initialdir="C:/gui/data",
            title="Save File",
            filetypes=(
                ("Dat Files", "*.dat"), 
                ("All Files", "*.*"))
            ) 
        if self.file_name:
            #delete currently open list
            self.my_list.delete(0, END)
            #open the file:
            self.input_file = open(self.file_name, 'rb')

            #load the data
            self.stuff = pickle.load(self.input_file)

            #output the stuff
            for self.item in self.stuff:
                self.my_list.insert(END, self.item)
    def clear_list(self):
        self.my_list.delete(0, END)

e = Event_Planner(root)
from tkcalendar import Calendar
import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
# ask user what type of even they want to add and when. 
class Cal:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()
    
        self.myButton = ttk.Button(master, text='Calendar with events', command=self.Events).pack(padx=10, pady=10)

    def Events(self):

        top = tk.Toplevel(root)

        cal = Calendar(top, selectmode='none')
        date = cal.datetime.today()

        cal.pack(fill="both", expand=True)
e = Cal(root)
root.mainloop()