
from tkcalendar import Calendar
import tkinter as tk
from tkinter import ttk
from tkinter import *

class Input:
    def __init__(self) -> None:
        pass
 
class Cal:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        top = tk.Toplevel(root)
        cal = Calendar(top, selectmode='none')
        date = cal.datetime.today()
        
        ans = 1
        while ans != 0:
            create = int(input('How many days from today is your reminder? '))
            color = input('Is your reminder for a meeting or for an assignment? ')
            cal.calevent_create(date+ cal.timedelta(days=create), 'Reminder', color)
            ans = int(input('Do you wish to set another reminder? (yes(1), no(0) '))
       
     
        cal.tag_config('meeting', background='purple', foreground='yellow')
        cal.tag_config('assignment', background='green', foreground='yellow')

        cal.pack(fill="both", expand=True)
        ttk.Label(top, text="Light Blue = Today\nGreen = Assignments \nPurple = Meetings").pack()

root = tk.Tk()
e = Cal(root)
root.mainloop()