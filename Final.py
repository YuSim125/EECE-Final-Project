from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle
import unittest

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
        """
        deleting item that has been marked by the user's 
        cursor and with the press of the button
        the item deletes itself. 
        
        """
        self.my_list.delete(ANCHOR)

    def add_item(self):
        """
        adds in any event that the user types in
        through the bar
        """
        self.my_list.insert(END, self.my_entry.get())
        self.my_entry.delete(0, END)

    def cross_off_item(self):
        """
        crosses out any item on the list
        that the user selects and marks it
        as a finished task.
        """
        #cross off item
        self.my_list.itemconfig(
            self.my_list.curselection(),
            fg="#dedede")
        #get rid of slection bar
        self.my_list.selection_clear(0, END)

    def uncross_item(self):
        """
        button that if selected a crossed event
        it will change back its font to show that
        the event has been uncrossed.
        """
        #cross off item
        self.my_list.itemconfig(
            self.my_list.curselection(),
            fg="#464646")
        #get rid of slection bar
        self.my_list.selection_clear(0, END)

    def delete_crossed_item(self):
        """
        deletes any selected events that 
        have the font of the crossed out
        event
        """
        self.count = 0
        while self.count < self.my_list.size():
            if self.my_list.itemcget(self.count, "fg") == "#dedede":
                self.my_list.delete(self.my_list.index(self.count))
            else:
                self.count += 1


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
                
    def clear_list(self):
        """
        clears the current list of the 
        planner and makes it all blank again
        """
        self.my_list.delete(0, END)

e = Event_Planner(root)



from tkcalendar import Calendar
import tkinter as tk
from tkinter import ttk
from tkinter import *


 
class Cal:
    """
    Creating a calendar that we can use
    to color code certain reminders that
    the user will input.
    """
    def __init__(self, root):
        myFrame = Frame(root)
        myFrame.pack()
        # creating the structure to the calendar
        top = tk.Toplevel(root)
        cal = Calendar(top, selectmode='none')
        date = cal.datetime.today()
        # while loop to figure out if the user wants to add more reminders or not
        # and display them onto the calendar
        ans = 1
        while ans != 0:
            create = int(input('How many days from today is your reminder? '))
            color = input('Is your reminder for a meeting or for an assignment? ')
            cal.calevent_create(date+ cal.timedelta(days=create), 'Reminder', color)
            ans = int(input('Do you wish to set another reminder? (yes(1), no(0) '))
       
        # creates the coloring for specific remiders from the user
        cal.tag_config('meeting', background='purple', foreground='yellow')
        cal.tag_config('assignment', background='green', foreground='yellow')

        cal.pack(fill="both", expand=True)
        # labeling the color coded boxes to let the user know which is which.
        ttk.Label(top, text="Light Blue = Today\nGreen = Assignments \nPurple = Meetings").pack()

root = tk.Tk()
e = Cal(root)
root.mainloop()

class TestCal(unittest.TestCase):
    def test_open_list(self):
        self.test_open_list(open_list(root),True)
    def test_delete_event(self):
        self.test_delete_event(delete_event(root),True)
    def test_add_event(self):
        self.test_add_event(add_event(root),True)
