from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

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


                
    def open_list(self):
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
                
    def clear_list(self):
        self.my_list.delete(0, END)

e = Event_Planner(root)
root.mainloop()