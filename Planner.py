from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle
from my_list import my_list

    

root = Tk()
root.title('Calendar Event List')
root.geometry("600x600")

    # Defining font
my_font = Font(
        family = "Times New Roman",
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

#functions
def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)
def cross_off_item():
    #cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")
    #get rid of slection bar
    my_list.selection_clear(0, END)
def uncross_item():
    #cross off item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646")
    #get rid of slection bar
    my_list.selection_clear(0, END)
def delete_crossed_item():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count += 1


def save_list():
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
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))
            else:
                count += 1
        # grab all the stuff from list
        stuff = my_list.get(0,END)
        # OPen the file
        output_file = open(file_name, 'wb')

        # Actually add teh stuff to teh file
        pickle.dump(stuff, output_file)


            
def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="C:/gui/data",
        title="Save File",
        filetypes=(
            ("Dat Files", "*.dat"), 
            ("All Files", "*.*"))
        ) 
    if file_name:
        #delete currently open list
        my_list.delete(0, END)
        #open the file:
        input_file = open(file_name, 'rb')

        #load the data
        stuff = pickle.load(input_file)

        #output the stuff
        for item in stuff:
            my_list.insert(END, item)
def clear_list():
    my_list.delete(0, END)

# create menu
my_menu = Menu(root)
root.config(menu=my_menu)     

#add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
# Add dropdown items
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=clear_list)

#add buttons
add_button = Button(button_frame, text="Add Event", command=add_item)
delete_button = Button(button_frame, text="Delete Event", command=delete_item)
cross_off_button = Button(button_frame, text="Cross off Event", command=cross_off_item)
uncross_button = Button(button_frame, text="Uncross Event", command=uncross_item)
delete_crossed_button = Button(button_frame, text="Delete Crossed Event", command=delete_crossed_item)

delete_button.grid(row=0, column=1, padx = 20)
add_button.grid(row=0, column=0)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx = 20)
delete_crossed_button.grid(row=0, column=4)

root.mainloop()