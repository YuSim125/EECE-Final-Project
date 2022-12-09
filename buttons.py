
from tkcalendar import Calendar
import tkinter as tk
from tkinter import ttk
from TodoList import Planner
# ask user what type of even they want to add and when. 
def Events():

    top = tk.Toplevel(root)

    cal = Calendar(top, selectmode='none')
    date = cal.datetime.today()
    cal.calevent_create(date+ cal.timedelta(days=2), 'Meeting', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=3), 'Homework Due', 'homework')

    cal.tag_config('reminder', background='red', foreground='yellow')

    cal.pack(fill="both", expand=True)
    ttk.Label(top, text="Light Blue = Today\n Red = Homework \n Blue = Meeting.").pack()

root = tk.Tk()
ttk.Button(root, text='Calendar with events', command=Events).pack(padx=10, pady=10)
ttk.Button(root, text='Event Planner', command=Planner).pack(padx=10, pady=10)
root.mainloop()